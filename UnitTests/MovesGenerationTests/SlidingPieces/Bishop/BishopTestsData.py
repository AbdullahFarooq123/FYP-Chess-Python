from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName

# Bishop Tests

white_bishop_test_data = {

    # normal move
    # 8	.  .  .  q  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  P  .  .  .  .  .
    # 2	.  B  .  .  .  .  .  .
    # 1	R  .  .  Q  K  B  .  .
    # 	a  b  c  d  e  f  g  h
    '3qk3/8/8/8/8/2P5/1B6/R2QKB2 w - - 1 1': [
        {
            'SOURCE_SQUARE': Positions.f1,
            'TARGET_SQUARE': Positions.e2,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f1,
            'TARGET_SQUARE': Positions.d3,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f1,
            'TARGET_SQUARE': Positions.c4,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f1,
            'TARGET_SQUARE': Positions.b5,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f1,
            'TARGET_SQUARE': Positions.a6,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f1,
            'TARGET_SQUARE': Positions.g2,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f1,
            'TARGET_SQUARE': Positions.h3,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.b2,
            'TARGET_SQUARE': Positions.a3,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.b2,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # capture move
    # 8	.  .  .  q  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  r  .  .  .  .
    # 3	p  .  .  .  .  .  .  n
    # 2	.  B  .  .  P  .  .  .
    # 1	R  .  .  Q  K  B  .  .
    # 	a  b  c  d  e  f  g  h
    '3qk3/8/8/8/3r4/p6n/1B2P3/R2QKB2 w - - 1 1': [
        {
            'SOURCE_SQUARE': Positions.b2,
            'TARGET_SQUARE': Positions.a3,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.b2,
            'TARGET_SQUARE': Positions.c3,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.b2,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.b2,
            'TARGET_SQUARE': Positions.d4,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f1,
            'TARGET_SQUARE': Positions.g2,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f1,
            'TARGET_SQUARE': Positions.h3,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # king in check
    # 8	.  .  .  q  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  r  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	R  .  B  .  K  B  .  .
    # 	a  b  c  d  e  f  g  h
    '3qk3/8/8/8/8/4r3/8/R1B1KB2 w - - 1 1': [
        {
            'SOURCE_SQUARE': Positions.f1,
            'TARGET_SQUARE': Positions.e2,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c1,
            'TARGET_SQUARE': Positions.e3,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],
    # king in check
    # 8	.  .  .  q  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  b
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	R  .  B  .  K  B  .  .
    # 	a  b  c  d  e  f  g  h
    '3qk3/8/8/8/7b/8/8/R1B1KB2 w - - 1 1': [],

    # pin check
    # 8	.  .  .  .  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  P  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	q  .  .  B  K  .  .  r
    # 	a  b  c  d  e  f  g  h
    '4k3/8/8/8/8/4P3/8/q2BK2r w - - 1 1': [],

}

black_bishop_test_data = {

    # normal move
    # 8	.  .  b  K  .  b  .  .
    # 7	.  .  .  .  p  .  .  .
    # 6	n  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  p  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	R  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '2bk1b2/4p3/n7/5p2/8/8/8/R3K3 b - - 1 1': [
        {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.b7,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.d7,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.e6,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f8,
            'TARGET_SQUARE': Positions.g7,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f8,
            'TARGET_SQUARE': Positions.h6,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # capture move
    # 8	.  .  b  k  .  b  .  .
    # 7	.  .  .  p  p  .  Q  .
    # 6	R  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '2bk1b2/3pp1Q1/R7/8/8/8/8/4K3 b - - 1 1': [
        {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.b7,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.a6,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f8,
            'TARGET_SQUARE': Positions.g7,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # king in check
    # 8	.  .  b  k  .  b  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  q
    # 4	.  .  .  R  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '2bk1b2/8/8/7q/3R4/8/8/4K3 b - - 1 1': [
        {
            'SOURCE_SQUARE': Positions.f8,
            'TARGET_SQUARE': Positions.d6,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.d7,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],

    # king in check
    # 8	.  .  b  k  .  b  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  R  .  .  .  Q
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '2bk1b2/8/8/8/3R3Q/8/8/4K3 b - - 1 1': [],

    # pin check
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  b  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  R  .  .  .  Q
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h

    '3k4/8/3b4/8/3R3Q/8/8/4K3 b - - 1 1': [],

    # pin check
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  b  .  b  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  R  .  .  .  Q
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h

    '3k4/8/3b1b2/8/3R3Q/8/8/4K3 b - - 1 1': [
        {
            'SOURCE_SQUARE': Positions.f6,
            'TARGET_SQUARE': Positions.e7,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f6,
            'TARGET_SQUARE': Positions.g5,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f6,
            'TARGET_SQUARE': Positions.h4,
            'PIECE_NAME': PieceName.BISHOP,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

}
