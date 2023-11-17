import numpy as np
from numpy import ndarray
from pandas import DataFrame

from NeuralNetworks.PositionEvaluatorCNN.Helpers.DataPreProcessingHelper.BoardStateToOneHotHelpers import fen_to_one_hot
from NeuralNetworks.PositionEvaluatorCNN.Helpers.DataPreProcessingHelper.DataEvalHelper import fix_eval_noise
from NeuralNetworks.PositionEvaluatorCNN.Helpers.DataPreProcessingHelper.GameFeatureToOneHotHelper import \
    get_game_state_features


def extract_board_feature_information(data: DataFrame) -> ndarray:
    board_features = []
    for fen in data['FEN']:
        board_features.append(fen_to_one_hot(fen))
    return np.array(board_features)


def extract_label_information(data: DataFrame) -> ndarray:
    labels = []
    for evaluation in data['Evaluation']:
        labels.append(fix_eval_noise(evaluation))
    return np.array(labels)


def extract_game_feature_information(data: DataFrame):
    game_state_features = []
    for fen in data['FEN']:
        game_state_features.append(get_game_state_features(fen))
    return np.array(game_state_features)
