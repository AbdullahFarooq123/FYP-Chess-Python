import math

from keras import Model
from tensorflow import keras


def configure_neural_network(model_path: str) -> Model:
    try:
        data_model = keras.models.load_model(model_path)
        print('Loaded existing model!')
    except OSError:
        print('No model found. Creating new model.')

        board_features_input = keras.layers.Input(shape=InputConfig.board_features_input_shape)
        board_features_input = keras.layers.Reshape(target_shape=InputConfig.board_features_reshape)(
            board_features_input)

        conv_2d = __make_conv2d_for_board_features(board_features_input)

        processed_board_feature_input = keras.layers.Flatten()(conv_2d)

        game_feature_input = keras.layers.Input(shape=InputConfig.game_features_input_shape)

        dense_layer_input = keras.layers.concatenate([processed_board_feature_input, game_feature_input])

        dense_layer = __make_dense_layers(dense_layer_input)

        output_layer = keras.layers.Dense(1, activation='linear')(dense_layer)

        data_model = keras.models.Model(inputs=[board_features_input, game_feature_input], outputs=output_layer,
                                        name='PositionEvaluator')

    metrics = [keras.metrics.MeanAbsoluteError(), keras.metrics.MeanSquaredError()]

    optimizer = keras.optimizers.Adam(learning_rate=0.001)

    loss_function = keras.losses.MeanSquaredError()

    data_model.compile(optimizer=optimizer,
                       loss=loss_function,
                       metrics=metrics)

    return data_model


def __make_conv2d_for_board_features(input_layer: keras.layers.Input):
    for i in range(1, Conv2dConfig.conv_2d_layer_count + 1):
        conv_layer = keras.layers.Conv2D(kernel_size=Conv2dConfig.conv_2d_kernel_size, padding='same',
                                         activation='relu',
                                         filters=Conv2dConfig.conv_2d_filter_count)(input_layer)
        conv_normalizer = keras.layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=1e-05)(conv_layer)
        input_layer = conv_normalizer
        Conv2dConfig.conv_2d_kernel_size = tuple(int(v / 2) for v in Conv2dConfig.conv_2d_kernel_size)
        Conv2dConfig.conv_2d_filter_count *= 2
    return input_layer


def __make_dense_layers(input_layer):
    threshold_values = abs(DenseConfig.dense_layer_count - DenseConfig.unit_step_count)
    for i in range(1, DenseConfig.dense_layer_count + 1):
        dense_layer = keras.layers.Dense(units=DenseConfig.dense_layer_units, activation='relu')(input_layer)
        input_layer = dense_layer
        if (DenseConfig.upper_threshold and i < threshold_values) or (
                DenseConfig.lower_threshold and i > DenseConfig.unit_step_count):
            continue
        DenseConfig.dense_layer_units /= 2
    return input_layer


class GameConfig:
    board_squares: int = 64
    unique_pieces: int = 6
    no_of_players: int = 2
    unique_castle_rights: int = 2
    enpassant_square_size: int = board_squares


class InputConfig:
    board_features_input_shape: tuple = (GameConfig.board_squares, GameConfig.unique_pieces * GameConfig.no_of_players)
    board_features_reshape: tuple = board_features_input_shape + (1,)
    game_features_input_shape: tuple = (
        GameConfig.no_of_players + (
                GameConfig.no_of_players * GameConfig.unique_castle_rights) + GameConfig.enpassant_square_size + 1 + 1,)


class Conv2dConfig:
    conv_2d_kernel_size: tuple = (8, 8)
    conv_2d_filter_count: int = 16
    conv_2d_layer_count: int = 3


class DenseConfig:
    dense_layer_count: int = 5
    min_dense_layer_units: int = 64
    max_dense_layer_units: int = 512
    __dense_layer_units: int = min_dense_layer_units * (2 ** (dense_layer_count - 1))
    upper_threshold: bool = True
    lower_threshold: bool = not upper_threshold
    dense_layer_units = __dense_layer_units if __dense_layer_units <= max_dense_layer_units else max_dense_layer_units
    unit_step_count: int = math.log2(max_dense_layer_units / min_dense_layer_units)
