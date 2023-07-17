from src.Enums.PositionsEnum import Positions
from src.Enums.PieceNameEnum import PieceName

# Queen's Move Tests

white_queen_test_data = {

    # Normal Queen Move
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  Q  .  .  .  .
    # 2 .  .  .  .  .  .  .  .
    # 1 .  .  .  .  K  .  .  .
    #   a  b  c  d  e  f  g  h
    '4k3/8/8/8/8/3Q4/8/4K3 w - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.a3,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.a6,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.b1,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.b3,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.b5,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.c2,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.c3,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.c4,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.d1,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.d2,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.d4,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.d5,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.d6,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.d7,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.d8,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.e2,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.e3,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.e4,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.f1,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.f3,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.f5,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.g3,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.g6,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.h3,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.h7,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # Capture move
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  b  .  .
    # 2 .  .  p  P  .  .  .  .
    # 1 .  R  .  Q  K  .  .  .
    #   a  b  c  d  e  f  g  h
    '4k3/8/8/8/8/5b2/2pP4/1R1QK3 w - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.d1,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d1,
            'TARGET_SQUARE': Positions.c2,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d1,
            'TARGET_SQUARE': Positions.e2,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d1,
            'TARGET_SQUARE': Positions.f3,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],
    # king in check
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  n  .  .
    # 2 .  .  .  P  .  .  .  .
    # 1 R  .  .  Q  K  .  .  .
    #   a  b  c  d  e  f  g  h

    '4k3/8/8/8/8/5n2/3P4/R2QK3 w - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.d1,
            'TARGET_SQUARE': Positions.f3,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # king in check
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  P  .  .  n  .
    # 1 R  .  .  Q  K  .  .  .
    #   a  b  c  d  e  f  g  h

    '4k3/8/8/8/8/8/3P2n1/R2QK3 w - - 0 1': [],

    # king in check
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  r  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  P  .  .  n  .
    # 1 R  .  B  Q  K  R  .  .
    #   a  b  c  d  e  f  g  h

    '4k3/8/8/4r3/8/8/3P4/R1BQKR2 w - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.d1,
            'TARGET_SQUARE': Positions.e2,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # pin check
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  r  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  Q  .  .  .
    # 1 .  .  .  .  K  .  .  .
    #   a  b  c  d  e  f  g  h

    '4k3/8/8/8/4r3/8/4Q3/4K3 w - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.e2,
            'TARGET_SQUARE': Positions.e3,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e2,
            'TARGET_SQUARE': Positions.e4,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

}

black_queen_test_data = {

    # Normal Queen Move
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  q  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  .  .  .
    # 1 .  .  .  .  K  .  .  .
    #   a  b  c  d  e  f  g  h
    '4k3/8/3q4/8/8/8/8/4K3 b - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.d6,
            'TARGET_SQUARE': Positions.a3,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d6,
            'TARGET_SQUARE': Positions.a6,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d6,
            'TARGET_SQUARE': Positions.b4,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d6,
            'TARGET_SQUARE': Positions.b6,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d6,
            'TARGET_SQUARE': Positions.b8,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d6,
            'TARGET_SQUARE': Positions.c5,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d6,
            'TARGET_SQUARE': Positions.c6,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d6,
            'TARGET_SQUARE': Positions.c7,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d6,
            'TARGET_SQUARE': Positions.d1,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d6,
            'TARGET_SQUARE': Positions.d2,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d6,
            'TARGET_SQUARE': Positions.d3,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.d4,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.d5,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.d7,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.d8,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.e5,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.e6,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.e7,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.f4,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.f6,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.g3,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.g6,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.h2,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d3,
            'TARGET_SQUARE': Positions.h6,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],
    # Capture move
    # 8 .  .  b  q  k  .  .  .
    # 7 .  .  P  p  .  .  .  .
    # 6 .  .  .  .  .  B  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  .  .  .
    # 1 .  .  .  .  K  .  .  .
    #   a  b  c  d  e  f  g  h
    '2bqk3/2Pp4/5B2/8/8/8/8/4K3 b - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.d8,
            'TARGET_SQUARE': Positions.e7,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d8,
            'TARGET_SQUARE': Positions.c7,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d8,
            'TARGET_SQUARE': Positions.f6,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],
    # king in check
    # 8 .  .  .  q  k  .  .  .
    # 7 .  .  P  .  .  .  .  .
    # 6 .  .  .  N  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  .  .  .
    # 1 .  .  .  .  K  .  .  .
    #   a  b  c  d  e  f  g  h
    '3qk3/2P5/3N4/8/8/8/8/4K3 b - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.d8,
            'TARGET_SQUARE': Positions.d6,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],
    # king in check
    # 8 .  .  .  .  k  .  .  R
    # 7 .  .  P  .  .  q  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  .  .  .
    # 1 .  .  .  .  K  .  .  .
    #   a  b  c  d  e  f  g  h
    '4k2R/2P2q2/8/8/8/8/8/4K3 b - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.f7,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f7,
            'TARGET_SQUARE': Positions.g8,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # pin check
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  q  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  B
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  .  .  .
    # 1 .  .  .  .  K  .  .  .
    #   a  b  c  d  e  f  g  h
    '4k3/5q2/8/7B/8/8/8/4K3 b - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.f7,
            'TARGET_SQUARE': Positions.g6,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f7,
            'TARGET_SQUARE': Positions.h5,
            'PIECE_NAME': PieceName.QUEEN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

}
