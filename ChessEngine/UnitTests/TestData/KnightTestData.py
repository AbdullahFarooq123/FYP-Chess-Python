from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PieceNameEnum import PieceName

# Bishop Tests

knight_move_generation = {

    # normal move
    # 8	.  .  .  q  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  N  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  N  .
    # 	a  b  c  d  e  f  g  h
    '3qk3/8/8/8/8/2N5/8/4K1N1 w - - 1 1': [
        {
            'SOURCE_SQUARE': Positions.c3,
            'TARGET_SQUARE': Positions.b1,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c3,
            'TARGET_SQUARE': Positions.a2,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c3,
            'TARGET_SQUARE': Positions.a4,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c3,
            'TARGET_SQUARE': Positions.b5,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c3,
            'TARGET_SQUARE': Positions.d1,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c3,
            'TARGET_SQUARE': Positions.d5,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

        {
            'SOURCE_SQUARE': Positions.c3,
            'TARGET_SQUARE': Positions.e2,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c3,
            'TARGET_SQUARE': Positions.e4,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.g1,
            'TARGET_SQUARE': Positions.h3,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.g1,
            'TARGET_SQUARE': Positions.e2,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.g1,
            'TARGET_SQUARE': Positions.f3,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],

    # capture move
    # 8	.  .  .  q  k .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  p  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  R  .
    # 2	N  .  .  .  .  K  .  .
    # 1	.  .  B  .  .  .  .  N
    # 	a  b  c  d  e  f  g  h
    '3qk3/8/8/8/1p6/6r1/N4K2/2B4N w - - 1 1': [
        {
            'SOURCE_SQUARE': Positions.a2,
            'TARGET_SQUARE': Positions.c3,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.a2,
            'TARGET_SQUARE': Positions.b4,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.h1,
            'TARGET_SQUARE': Positions.g3,
            'PIECE_NAME': PieceName.KNIGHT,
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
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  K  .  r  .
    # 1	.  .  .  .  .  .  .  N
    # 	a  b  c  d  e  f  g  h
    '3qk3/8/8/8/8/8/4K1r1/7N w - - 1 1': [
        {
            'SOURCE_SQUARE': Positions.h1,
            'TARGET_SQUARE': Positions.f2,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # king in check
    # 8	.  .  .  q  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  N  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  N  .  .  K  .  r  .
    # 1	.  .  .  .  .  .  .  .
    # 	a  b  c  d  e  f  g  h
    '3qk3/8/8/4N3/8/8/1N2K1r1/8 w - - 1 1': [

    ],

    # king in check 
    # 8	.  .  .  q  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  N  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  N  .  .  K  .  r  .
    # 1	.  .  .  .  .  .  .  .
    # 	a  b  c  d  e  f  g  h
    '3qk3/8/8/7b/5N2/8/4K3/8 w - - 1 1': [
        {
            'SOURCE_SQUARE': Positions.f4,
            'TARGET_SQUARE': Positions.h5,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],
    # pin check
    # 8	.  .  .  q  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  K  .  N  .  .  r
    # 1	.  .  .  .  .  .  .  .
    # 	a  b  c  d  e  f  g  h

    '3qk3/8/8/8/8/8/2K1N2r/8 b - - 1 1': [],

    # pin check
    # 8	.  .  .  q  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	b  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  N  .  .  .  .  .
    # 1	.  .  .  K  .  .  .  .
    # 	a  b  c  d  e  f  g  h

    '3qk3/8/8/8/b7/8/2N5/3K4 w - - 1 1': [],

}

knight_attacks = {
    'h1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'g1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 1 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 1 0 
        0 0 0 1 0 0 0 1 
        0 0 0 0 0 0 0 0 
        ''',
    'e1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 1 0 0 
        0 0 1 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 1 0 0 0 
        0 1 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 1 0 0 0 0 
        1 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 0 1 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 0 
        ''',
    'g2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 1 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 0 0 
        ''',
    'f2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 1 0 
        0 0 0 1 0 0 0 1 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 1 
        ''',
    'e2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 1 0 0 
        0 0 1 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 1 0 
        ''',
    'd2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 1 0 0 0 
        0 1 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 1 0 0 
        ''',
    'c2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 1 0 0 0 0 
        1 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        1 0 0 0 1 0 0 0 
        ''',
    'b2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 0 1 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        ''',
    'a2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        ''',
    'h3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 1 0 
        ''',
    'g3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 1 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 1 0 1 
        ''',
    'f3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 1 0 
        0 0 0 1 0 0 0 1 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 1 
        0 0 0 0 1 0 1 0 
        ''',
    'e3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 1 0 0 
        0 0 1 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 1 0 
        0 0 0 1 0 1 0 0 
        ''',
    'd3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 1 0 0 0 
        0 1 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 1 0 0 
        0 0 1 0 1 0 0 0 
        ''',
    'c3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 1 0 0 0 0 
        1 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        1 0 0 0 1 0 0 0 
        0 1 0 1 0 0 0 0 
        ''',
    'b3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 0 1 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        1 0 1 0 0 0 0 0 
        ''',
    'a3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        ''',
    'h4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'g4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 1 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 1 0 1 
        0 0 0 0 0 0 0 0 
        ''',
    'f4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 1 0 
        0 0 0 1 0 0 0 1 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 1 
        0 0 0 0 1 0 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 1 0 0 
        0 0 1 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 1 0 
        0 0 0 1 0 1 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 1 0 0 0 
        0 1 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 1 0 0 
        0 0 1 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 1 0 0 0 0 
        1 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        1 0 0 0 1 0 0 0 
        0 1 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 0 1 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        1 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'g5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 1 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 1 0 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 1 0 
        0 0 0 1 0 0 0 1 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 1 
        0 0 0 0 1 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 1 0 0 
        0 0 1 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 1 0 
        0 0 0 1 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 1 0 1 0 0 0 
        0 1 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 1 0 0 
        0 0 1 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c5':
        '''
        0 0 0 0 0 0 0 0 
        0 1 0 1 0 0 0 0 
        1 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        1 0 0 0 1 0 0 0 
        0 1 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b5':
        '''
        0 0 0 0 0 0 0 0 
        1 0 1 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        1 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a5':
        '''
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h6':
        '''
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'g6':
        '''
        0 0 0 0 0 1 0 1 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 1 0 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f6':
        '''
        0 0 0 0 1 0 1 0 
        0 0 0 1 0 0 0 1 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 1 
        0 0 0 0 1 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e6':
        '''
        0 0 0 1 0 1 0 0 
        0 0 1 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 1 0 
        0 0 0 1 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd6':
        '''
        0 0 1 0 1 0 0 0 
        0 1 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 1 0 0 
        0 0 1 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c6':
        '''
        0 1 0 1 0 0 0 0 
        1 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        1 0 0 0 1 0 0 0 
        0 1 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b6':
        '''
        1 0 1 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        1 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a6':
        '''
        0 1 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h7':
        '''
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'g7':
        '''
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 1 0 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f7':
        '''
        0 0 0 1 0 0 0 1 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 1 
        0 0 0 0 1 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e7':
        '''
        0 0 1 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 1 0 
        0 0 0 1 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd7':
        '''
        0 1 0 0 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 1 0 0 
        0 0 1 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c7':
        '''
        1 0 0 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        1 0 0 0 1 0 0 0 
        0 1 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b7':
        '''
        0 0 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        1 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a7':
        '''
        0 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h8':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 0 0 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'g8':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 0 0 0 
        0 0 0 0 0 1 0 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f8':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 1 
        0 0 0 0 1 0 1 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e8':
        '''
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 1 0 
        0 0 0 1 0 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd8':
        '''
        0 0 0 0 0 0 0 0 
        0 1 0 0 0 1 0 0 
        0 0 1 0 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c8':
        '''
        0 0 0 0 0 0 0 0 
        1 0 0 0 1 0 0 0 
        0 1 0 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b8':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 1 0 0 0 0 
        1 0 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a8':
        '''
        0 0 0 0 0 0 0 0 
        0 0 1 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
}
