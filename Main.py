# from NeuralNetworks.PositionEvaluatorCNN.Controllers.ProcessDataController import load_data_in_tensor, load_data
from ChessEngine.UnitTests.Controllers.GamePlayTestController import run_game_play_tests
from ChessEngine.UnitTests.Controllers.UnitTestController import UnitTestEngine
from ChessEngine.UnitTests.Enums.TestOfEnum import TestsOf
from ChessEngine.src.Controllers import PreCalculationsController
from ChessEngine.src.Helpers.BeautifyHelpers.GameBeautifyHelpers import print_game_board
from ChessEngine.src.Helpers.FenHelpers.FenDecryptHelpers import decrypt_fen
from ChessEngine.src.Models.FenModel import Fen
from NeuralNetworks.PositionEvaluatorCNN import Config
from NeuralNetworks.PositionEvaluatorCNN.Controllers.LoadDataController import load_data
from NeuralNetworks.PositionEvaluatorCNN.Controllers.NeuralNetworkController import PositionEvalNN
from NeuralNetworks.PositionEvaluatorCNN.Helpers.DataPreProcessingHelper.DataFenFeatureHelper import get_feature_vector


def run_unit_test():
    u_engine = UnitTestEngine(show_only_tests=TestsOf.FAILED, print_test_cases=TestsOf.FAILED,
                              print_test_case_details=TestsOf.FAILED)
    u_engine.run_tests()
    u_engine.print_tests()
    run_game_play_tests()


def run_migrations():
    PreCalculationsController.init_migrations()


def run_testing():
    # eval = PositionEvalNN(start_learning_rate=Config.start_learning_rate,
    #                       min_learning_rate=Config.min_learning_rate,
    #                       max_learning_rate=Config.max_learning_rate,
    #                       ramp_up_epochs=Config.ramp_up_epochs,
    #                       sustain_epochs=Config.sustain_epochs,
    #                       exp_decay=Config.exp_decay,
    #                       epochs=Config.epochs,
    #                       save_interval=Config.save_interval,
    #                       training_data_limit=Config.training_data_limit)
    # eval.train_position_evaluator(model_path='D:\\Position Evaluator(loss 6.09 - mean_absolute_error 1.8359).keras')
    # import tensorflow as tf
    # import numpy as np
    # trained_model = tf.keras.models.load_model('D:\\Position Evaluator.keras')
    # values = []
    # while True:
    #     fen = input('Please enter fen : ')
    #     feature_vector = get_feature_vector(fen)
    #     value = np.array(feature_vector)
    #     features = np.array([value[:6]])
    #     board = np.array([value[6:]])
    #     prediction = trained_model.predict([board, features])
    #     print(f'{fen} : {prediction}')
    import chess
    import chess.engine

    engine = chess.engine.SimpleEngine.popen_uci(
        "C:\\Users\\Dev\\Downloads\\stockfish-windows-x86-64-avx2\\stockfish\\stockfish-windows-x86-64-avx2.exe")

    while True:
        fen = input('Please enter fen : ')
        board = chess.Board(fen)
        info = engine.analyse(board, chess.engine.Limit(depth=22))
        score = info['score'].replace('PovScore', '').replace('(', '').replace(')')
        print(info['score'])
    # Score: PovScore(Mate(+1), WHITE)

    engine.quit()


if __name__ == '__main__':
    run_testing()
    # run_unit_test()
    # run_migrations()
