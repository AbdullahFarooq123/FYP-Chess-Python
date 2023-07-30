from keras import Model
from tensorflow import keras

from NeuralNetworks.PositionEvaluatorCNN import Config


def configure_neural_network(model_path: str) -> Model:
    try:
        data_model = keras.models.load_model(model_path)
        print('Loaded existing model!')
    except OSError:
        print('No model found. Creating new model.')
        board_feature_input = keras.layers.Input(shape=Config.board_feature_input_shape)
        reshape_board_feature = keras.layers.Reshape(target_shape=(8, 8, 1))(board_feature_input)
        conv_layer_1 = keras.layers.Conv2D(kernel_size=(8, 8), padding="same", activation="relu",
                                           filters=Config.filter_count,
                                           input_shape=(8, 8, 1))(reshape_board_feature)
        normalization_layer_1 = keras.layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=1e-05)(conv_layer_1)
        conv_layer_2 = keras.layers.Conv2D(kernel_size=(8, 8), padding="same", activation="relu",
                                           filters=Config.filter_count,
                                           input_shape=(8, 8, 1))(normalization_layer_1)
        normalization_layer_2 = keras.layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=1e-05)(conv_layer_2)
        input_for_dense = keras.layers.Flatten()(normalization_layer_2)
        player_feature_input = keras.layers.Input(shape=Config.player_feature_input_shape)

        dense_layer_input = keras.layers.concatenate([input_for_dense, player_feature_input])

        dense_layer_1 = keras.layers.Dense(1024, activation='relu')(dense_layer_input)
        dense_layer_2 = keras.layers.Dense(512, activation='relu')(dense_layer_1)
        dense_layer_3 = keras.layers.Dense(256, activation='relu')(dense_layer_2)
        dense_layer_4 = keras.layers.Dense(256, activation='relu')(dense_layer_3)

        output_layer = keras.layers.Dense(1, activation='linear')(dense_layer_4)

        data_model = keras.models.Model(inputs=[board_feature_input, player_feature_input], outputs=output_layer,
                                        name='Position_Evaluator')

    metrics = [keras.metrics.MeanAbsoluteError(), keras.metrics.SparseCategoricalAccuracy(), keras.metrics.Accuracy(),
               keras.metrics.CategoricalAccuracy(), keras.metrics.BinaryAccuracy()]

    optimizer = keras.optimizers.Adam()

    loss_function = keras.losses.MeanSquaredError()

    data_model.compile(optimizer=optimizer,
                       loss=loss_function,
                       metrics=metrics)

    return data_model
