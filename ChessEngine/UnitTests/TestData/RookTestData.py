from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PieceNameEnum import PieceName

# Rook tests

rook_move_generations = {

    # normal move
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  P  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  R  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h

    '3k4/8/4P3/8/8/4R3/8/4K3 w - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.e2,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.e4,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.e5,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.a3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.b3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.c3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.d3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.f3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.g3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.h3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # capture move Check
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	r  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	R  .  .  .  n  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	R  .  .  Q  K  .  .  .
    # 	a  b  c  d  e  f  g  h

    '3k4/8/8/r7/8/R3n3/8/R2QK3 w - - 0 1': [

        {
            'SOURCE_SQUARE': Positions.a1,
            'TARGET_SQUARE': Positions.a2,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.a1,
            'TARGET_SQUARE': Positions.b1,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.a1,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.a3,
            'TARGET_SQUARE': Positions.a4,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.a3,
            'TARGET_SQUARE': Positions.a5,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.a3,
            'TARGET_SQUARE': Positions.b3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.a3,
            'TARGET_SQUARE': Positions.c3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.a3,
            'TARGET_SQUARE': Positions.a2,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.a3,
            'TARGET_SQUARE': Positions.d3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.a3,
            'TARGET_SQUARE': Positions.e3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],
    # king in check
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	R  .  .  .  .  n  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	R  .  .  Q  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '3k4/8/8/8/8/R4n2/8/R2QK3 w - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.a3,
            'TARGET_SQUARE': Positions.f3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # king in check
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  b  .
    # 2	.  .  .  .  .  .  R  .
    # 1	.  .  .  Q  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '3k4/8/8/8/8/6b1/6R1/3QK3 w - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.g2,
            'TARGET_SQUARE': Positions.g3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.g2,
            'TARGET_SQUARE': Positions.f2,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # pin check
    # 8	.  .  .  .  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  b
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  R  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h

    '4k3/8/8/8/7b/8/5R2/4K3 w - - 0 1': [],

    # pin check
    # 8	.  .  .  .  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  b
    # 3	.  .  .  n  .  .  .  .
    # 2	.  .  .  R  .  R  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h

    '4k3/8/8/8/7b/3n4/3R1R2/4K3 w - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.d2,
            'TARGET_SQUARE': Positions.d3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # pin check
    # 8	.  .  .  .  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  b
    # 3	.  .  .  .  .  .  .  .
    # 2	.  P  .  .  .  R  .  .
    # 1	.  R  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h

    '4k3/8/8/8/7b/8/1P3R2/1R2K3 w - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.b1,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.b1,
            'TARGET_SQUARE': Positions.a1,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.b1,
            'TARGET_SQUARE': Positions.d1,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

}

rook_attack_counts = [
    12, 11, 11, 11, 11, 11, 11, 12,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    12, 11, 11, 11, 11, 11, 11, 12
]

rook_attacks_exc_ends = {
    'h1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 1 1 1 1 1 1 0 
        ''',
    'g1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 1 1 1 1 1 0 0 
        ''',
    'f1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 1 1 1 1 0 1 0 
        ''',
    'e1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 1 1 1 0 1 1 0 
        ''',
    'd1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 1 1 0 1 1 1 0 
        ''',
    'c1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 1 0 1 1 1 1 0 
        ''',
    'b1':
        '''
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 1 1 1 1 1 0 
        ''',
    'a1':
        '''
        0 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 0 
        ''',
    'h2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'g2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 1 1 1 1 1 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 1 1 1 1 0 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 1 1 1 0 1 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 1 1 0 1 1 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 1 0 1 1 1 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b2':
        '''
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 1 1 1 1 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a2':
        '''
        0 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 0 
        ''',
    'g3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 1 1 1 1 1 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 1 1 1 1 0 1 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 1 1 1 0 1 1 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 1 1 0 1 1 1 0 
        0 0 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 1 0 1 1 1 1 0 
        0 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b3':
        '''
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 1 1 1 1 1 0 
        0 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a3':
        '''
        0 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 0 
        1 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 0 
        ''',
    'g4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 1 1 1 1 1 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 1 1 1 1 0 1 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 1 1 1 0 1 1 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 1 1 0 1 1 1 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 1 0 1 1 1 1 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b4':
        '''
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 1 1 1 1 1 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a4':
        '''
        0 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 0 
        ''',
    'g5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 1 1 1 1 1 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 1 1 1 1 0 1 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 1 1 1 0 1 1 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 1 1 0 1 1 1 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 1 0 1 1 1 1 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b5':
        '''
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 1 1 1 1 1 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a5':
        '''
        0 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h6':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 1 
        0 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 0 
        ''',
    'g6':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 0 
        0 1 1 1 1 1 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f6':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 0 
        0 1 1 1 1 0 1 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e6':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 0 0 
        0 1 1 1 0 1 1 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd6':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 1 1 0 1 1 1 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c6':
        '''
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 1 0 1 1 1 1 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b6':
        '''
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 1 1 1 1 1 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a6':
        '''
        0 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h7':
        '''
        0 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 0 
        ''',
    'g7':
        '''
        0 0 0 0 0 0 0 0 
        0 1 1 1 1 1 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f7':
        '''
        0 0 0 0 0 0 0 0 
        0 1 1 1 1 0 1 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e7':
        '''
        0 0 0 0 0 0 0 0 
        0 1 1 1 0 1 1 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd7':
        '''
        0 0 0 0 0 0 0 0 
        0 1 1 0 1 1 1 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c7':
        '''
        0 0 0 0 0 0 0 0 
        0 1 0 1 1 1 1 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b7':
        '''
        0 0 0 0 0 0 0 0 
        0 0 1 1 1 1 1 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a7':
        '''
        0 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h8':
        '''
        0 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 0 
        ''',
    'g8':
        '''
        0 1 1 1 1 1 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f8':
        '''
        0 1 1 1 1 0 1 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e8':
        '''
        0 1 1 1 0 1 1 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd8':
        '''
        0 1 1 0 1 1 1 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c8':
        '''
        0 1 0 1 1 1 1 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b8':
        '''
        0 0 1 1 1 1 1 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a8':
        '''
        0 1 1 1 1 1 1 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
}

rook_attacks_inc_ends = {
    'h1':
        '''
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        1 1 1 1 1 1 1 0 
        ''',
    'g1':
        '''
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        1 1 1 1 1 1 0 1 
        ''',
    'f1':
        '''
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        1 1 1 1 1 0 1 1 
        ''',
    'e1':
        '''
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        1 1 1 1 0 1 1 1 
        ''',
    'd1':
        '''
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        1 1 1 0 1 1 1 1 
        ''',
    'c1':
        '''
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        1 1 0 1 1 1 1 1 
        ''',
    'b1':
        '''
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        1 0 1 1 1 1 1 1 
        ''',
    'a1':
        '''
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 1 
        ''',
    'h2':
        '''
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        1 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 1 
        ''',
    'g2':
        '''
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        1 1 1 1 1 1 0 1 
        0 0 0 0 0 0 1 0 
        ''',
    'f2':
        '''
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        1 1 1 1 1 0 1 1 
        0 0 0 0 0 1 0 0 
        ''',
    'e2':
        '''
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        1 1 1 1 0 1 1 1 
        0 0 0 0 1 0 0 0 
        ''',
    'd2':
        '''
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        1 1 1 0 1 1 1 1 
        0 0 0 1 0 0 0 0 
        ''',
    'c2':
        '''
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        1 1 0 1 1 1 1 1 
        0 0 1 0 0 0 0 0 
        ''',
    'b2':
        '''
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        1 0 1 1 1 1 1 1 
        0 1 0 0 0 0 0 0 
        ''',
    'a2':
        '''
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 1 
        1 0 0 0 0 0 0 0 
        ''',
    'h3':
        '''
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        1 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        ''',
    'g3':
        '''
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        1 1 1 1 1 1 0 1 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        ''',
    'f3':
        '''
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        1 1 1 1 1 0 1 1 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        ''',
    'e3':
        '''
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        1 1 1 1 0 1 1 1 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        ''',
    'd3':
        '''
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        1 1 1 0 1 1 1 1 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        ''',
    'c3':
        '''
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        1 1 0 1 1 1 1 1 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        ''',
    'b3':
        '''
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        1 0 1 1 1 1 1 1 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        ''',
    'a3':
        '''
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 1 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        ''',
    'h4':
        '''
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        1 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        ''',
    'g4':
        '''
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        1 1 1 1 1 1 0 1 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        ''',
    'f4':
        '''
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        1 1 1 1 1 0 1 1 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        ''',
    'e4':
        '''
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        1 1 1 1 0 1 1 1 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        ''',
    'd4':
        '''
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        1 1 1 0 1 1 1 1 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        ''',
    'c4':
        '''
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        1 1 0 1 1 1 1 1 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        ''',
    'b4':
        '''
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        1 0 1 1 1 1 1 1 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        ''',
    'a4':
        '''
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 1 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        ''',
    'h5':
        '''
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        1 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        ''',
    'g5':
        '''
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        1 1 1 1 1 1 0 1 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        ''',
    'f5':
        '''
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        1 1 1 1 1 0 1 1 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        ''',
    'e5':
        '''
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        1 1 1 1 0 1 1 1 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        ''',
    'd5':
        '''
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        1 1 1 0 1 1 1 1 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        ''',
    'c5':
        '''
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        1 1 0 1 1 1 1 1 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        ''',
    'b5':
        '''
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        1 0 1 1 1 1 1 1 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        ''',
    'a5':
        '''
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 1 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        ''',
    'h6':
        '''
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        1 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        ''',
    'g6':
        '''
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        1 1 1 1 1 1 0 1 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        ''',
    'f6':
        '''
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        1 1 1 1 1 0 1 1 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        ''',
    'e6':
        '''
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        1 1 1 1 0 1 1 1 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        ''',
    'd6':
        '''
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        1 1 1 0 1 1 1 1 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        ''',
    'c6':
        '''
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        1 1 0 1 1 1 1 1 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        ''',
    'b6':
        '''
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        1 0 1 1 1 1 1 1 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        ''',
    'a6':
        '''
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 1 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        ''',
    'h7':
        '''
        0 0 0 0 0 0 0 1 
        1 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        ''',
    'g7':
        '''
        0 0 0 0 0 0 1 0 
        1 1 1 1 1 1 0 1 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        ''',
    'f7':
        '''
        0 0 0 0 0 1 0 0 
        1 1 1 1 1 0 1 1 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        ''',
    'e7':
        '''
        0 0 0 0 1 0 0 0 
        1 1 1 1 0 1 1 1 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        ''',
    'd7':
        '''
        0 0 0 1 0 0 0 0 
        1 1 1 0 1 1 1 1 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        ''',
    'c7':
        '''
        0 0 1 0 0 0 0 0 
        1 1 0 1 1 1 1 1 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        ''',
    'b7':
        '''
        0 1 0 0 0 0 0 0 
        1 0 1 1 1 1 1 1 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        ''',
    'a7':
        '''
        1 0 0 0 0 0 0 0 
        0 1 1 1 1 1 1 1 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        ''',
    'h8':
        '''
        1 1 1 1 1 1 1 0 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        0 0 0 0 0 0 0 1 
        ''',
    'g8':
        '''
        1 1 1 1 1 1 0 1 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 0 
        ''',
    'f8':
        '''
        1 1 1 1 1 0 1 1 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 1 0 0 
        ''',
    'e8':
        '''
        1 1 1 1 0 1 1 1 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 1 0 0 0 
        ''',
    'd8':
        '''
        1 1 1 0 1 1 1 1 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 1 0 0 0 0 
        ''',
    'c8':
        '''
        1 1 0 1 1 1 1 1 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        ''',
    'b8':
        '''
        1 0 1 1 1 1 1 1 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        ''',
    'a8':
        '''
        0 1 1 1 1 1 1 1 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        1 0 0 0 0 0 0 0 
        '''
}
