import numpy as np
import pandas as pd
from numpy import ndarray
from pandas import DataFrame

from NeuralNetworks.PositionEvaluatorCNN import Config
from NeuralNetworks.PositionEvaluatorCNN.Helpers.DataPreProcessingHelper.DataEvalHelper import fix_eval_noise
from NeuralNetworks.PositionEvaluatorCNN.Helpers.DataPreProcessingHelper.DataFenFeatureHelper import get_feature_vector


def load_data(limit, use_limit: bool = True) -> [[ndarray, ndarray], ndarray]:
    chess_data: DataFrame = pd.read_csv(Config.training_data_path)
    if use_limit:
        chess_data = chess_data.head(limit)

    data_features: DataFrame = __extract_feature_information(data=chess_data)
    data_labels: ndarray = __extract_label_information(data=chess_data)
    input_board, input_meta = __extract_input_and_meta_information(data=data_features)

    return [input_board, input_meta], data_labels


def __extract_feature_information(data: DataFrame) -> DataFrame:
    fens: DataFrame = data.drop(columns=data.iloc[:, [1]])
    data_features: DataFrame = fens.apply(get_feature_vector, axis=1)
    data_features: DataFrame = data_features.apply(pd.Series)
    return data_features


def __extract_label_information(data: DataFrame) -> ndarray:
    data_labels: DataFrame = data.astype(str)
    data_labels: DataFrame = data_labels.apply(lambda x: fix_eval_noise(x['FEN'], x['Evaluation']), axis=1)
    return np.array(data_labels)


def __extract_input_and_meta_information(data: DataFrame) -> [ndarray, ndarray]:
    # The board is actually composed of white-features + black-features + board-features
    # w[O-O , O-O-O, #] + b[O-O , O-O-O, #] + [(board_features)]
    # w = white
    # b = black
    # O-O = Can King Side Castle?
    # O-O-O = Can Queen Side Castle?
    # board_features = Are actually each piece replaced by an integer value
    #                  negative for black and positive for white and 0 for space
    input_board: DataFrame = data.drop(columns=data.iloc[:, range(6)])
    input_meta: DataFrame = data.iloc[:, range(6)]
    # Convert the dataframes to numpy array to make them
    # ready injected to the Neural Networks
    input_board: ndarray = np.array(input_board)
    input_meta: ndarray = np.array(input_meta)

    return input_board, input_meta
