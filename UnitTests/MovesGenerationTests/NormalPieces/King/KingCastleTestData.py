from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName

white_king_castle_test_data = {
    '8/8/8/1r6/8/8/8/R3K2R w KQ - 0 1': [
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.g1,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': True,
        },
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': True,
        },
    ],
    '8/8/8/2r3r1/8/8/8/R3K2R w KQ - 0 1': [],
    '8/8/8/2r3r1/8/8/6P1/R3K2R w KQ - 0 1': [
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.g1,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': True,
        },
    ],
    '8/8/8/2r3r1/3b4/8/6P1/R3K2R w KQ - 0 1': [],
    '8/8/8/2r3r1/3b4/2P5/5PP1/R3K2R w KQ - 0 1': [
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.g1,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': True,
        },
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': True,
        },
    ],
    '8/8/8/1r6/8/8/8/R3K2R w - - 0 1': [],
}
black_king_castle_test_data = {}
