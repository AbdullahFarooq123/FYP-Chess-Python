# # import os
# #
# # import keras
# # import numpy as np
# # import pandas as pd
# # import tensorflow.python.keras
# import keras
# import numpy as np
# import pandas as pd
#
# from ChessEngine.UnitTests.Controllers.GamePlayTestController import run_game_play_tests
# from ChessEngine.UnitTests.Controllers.UnitTestController import UnitTestEngine
# from ChessEngine.UnitTests.Enums.TestOfEnum import TestsOf
# from ChessEngine.src.Controllers import PreCalculationsController
# from NeuralNetworks.PositionEvaluatorCNN.Controllers.LoadDataController import extract_board_feature_information, \
#     extract_label_information, extract_game_feature_information
# from NeuralNetworks.PositionEvaluatorCNN.Helpers.DataPreProcessingHelper.BoardStateToOneHotHelpers import fen_to_one_hot
# from NeuralNetworks.PositionEvaluatorCNN.Helpers.DataPreProcessingHelper.GameFeatureToOneHotHelper import \
#     get_game_state_features
#
#
# # from NeuralNetworks.PositionEvaluatorCNN.Helpers.DataPreProcessingHelper.BoardStateToOneHotHelpers import fen_to_one_hot
# # from NeuralNetworks.PositionEvaluatorCNN.Helpers.DataPreProcessingHelper.GameFeatureToOneHotHelper import \
# #     get_game_state_features
#
#
# def run_unit_test():
#     u_engine = UnitTestEngine(show_only_tests=TestsOf.FAILED, print_test_cases=TestsOf.FAILED,
#                               print_test_case_details=TestsOf.FAILED)
#     u_engine.run_tests()
#     u_engine.print_tests()
#     run_game_play_tests()
#
#
# def run_migrations():
#     PreCalculationsController.init_migrations()
#
#
# def run_testing():
#     model = keras.models.load_model('Model_5.keras')
#     while True:
#         fen = input("Please enter fen : ")
#         board_state = np.reshape(np.array(fen_to_one_hot(fen)).astype(float), (1, 64, 12, 1))
#         game_state = np.reshape(np.array(get_game_state_features(fen)).astype(float), (1, 72, 1))
#         value = model.predict([board_state, game_state])
#         print(value)
#
#
# if __name__ == '__main__':
#     run_testing()
#     # run_unit_test()
#     # run_migrations())
print(max(0,-1))