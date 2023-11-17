from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PieceNameEnum import PieceName

# King's Move Tests 

king_move_generation = {

    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  .  .  .
    # 1 R  .  .  .  K  .  .  R

    #   a  b  c  d  e  f  g  h

    '4k3/8/8/8/8/8/8/R3K2R w KQ - 0 1': [
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.e2,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.d2,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.d1,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.f2,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.f1,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

        # # Queen side Castling
        # {
        #     'SOURCE_SQUARE': Positions.e1,
        #     'TARGET_SQUARE': Positions.c1,
        #     'PIECE_NAME': PieceName.KING,
        #     'PROMOTION_PIECE_NAME': PieceName.NONE,
        #     'CAPTURE_FLAG': False,
        #     'DOUBLE_PUSH_FLAG': False,
        #     'EN_PASSANT_FLAG': False,
        #     'CASTLE_FLAG': True,
        # },
        # # king side Castling 
        # {
        #     'SOURCE_SQUARE': Positions.e1,
        #     'TARGET_SQUARE': Positions.g1,
        #     'PIECE_NAME': PieceName.KING,
        #     'PROMOTION_PIECE_NAME': PieceName.NONE,
        #     'CAPTURE_FLAG': False,
        #     'DOUBLE_PUSH_FLAG': False,
        #     'EN_PASSANT_FLAG': False,
        #     'CASTLE_FLAG': True,
        # },
    ],

    # Blocked by white piece
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  P  .  .  .
    # 1 .  .  .  .  K  .  .  .

    #   a  b  c  d  e  f  g  h

    '4k3/8/8/8/8/8/4P3/4K3 w - - 0 1': [

        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.d2,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.d1,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.f2,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.f1,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],

    # Moving squares under attack
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  r  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  b  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  .  .  .
    # 1 .  .  .  .  K  .  .  .

    #   a  b  c  d  e  f  g  h

    '4k3/8/3r4/8/6b1/8/8/4K3 w - - 0 1': [

        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.f2,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.f1,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],

    # All Moving squares under attack
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  r  .  r  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  b  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  .  .  .
    # 1 R  .  .  .  K  .  .  .
    #   a  b  c  d  e  f  g  h

    '4k3/8/3r1r2/8/6b1/8/8/R3K3 w - - 0 1': [],
    # Capture Move
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  r  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  b  .  .
    # 1 R  .  .  .  K  .  .  .
    #   a  b  c  d  e  f  g  h

    '4k3/8/8/3r4/8/8/5b2/R3K3 w - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.e2,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.f1,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.f2,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],
    # Invalid Capture Move
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  r  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  b  .  .
    # 1 R  .  .  .  K  .  .  .
    #   a  b  c  d  e  f  g  h

    '4k3/8/8/3r1r2/8/8/5b2/R3K3 w - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.e2,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e1,
            'TARGET_SQUARE': Positions.f1,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],

    # King under check
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  r  .  .  .  b
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  R  .  K  .  .  .
    # 1 r  .  .  .  .  .  .  .
    #   a  b  c  d  e  f  g  h

    '4k3/8/8/3r3b/8/8/4K3/r7 w - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.e2,
            'TARGET_SQUARE': Positions.e3,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e2,
            'TARGET_SQUARE': Positions.f2,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],

}

king_attacks = {
    'h1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 1 
        0 0 0 0 0 0 1 0 
        ''',
    'g1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 1 1 
        0 0 0 0 0 1 0 1 
        ''',
    'f1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 1 1 0 
        0 0 0 0 1 0 1 0 
        ''',
    'e1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 1 1 0 0 
        0 0 0 1 0 1 0 0 
        ''',
    'd1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 1 1 0 0 0 
        0 0 1 0 1 0 0 0 
        ''',
    'c1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 1 1 1 0 0 0 0 
        0 1 0 1 0 0 0 0 
        ''',
    'b1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 1 1 0 0 0 0 0 
        1 0 1 0 0 0 0 0 
        ''',
    'a1':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        ''',
    'h2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 1 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 1 
        ''',
    'g2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 1 1 
        0 0 0 0 0 1 0 1 
        0 0 0 0 0 1 1 1 
        ''',
    'f2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 1 1 0 
        0 0 0 0 1 0 1 0 
        0 0 0 0 1 1 1 0 
        ''',
    'e2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 1 1 0 0 
        0 0 0 1 0 1 0 0 
        0 0 0 1 1 1 0 0 
        ''',
    'd2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 1 1 0 0 0 
        0 0 1 0 1 0 0 0 
        0 0 1 1 1 0 0 0 
        ''',
    'c2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 1 1 1 0 0 0 0 
        0 1 0 1 0 0 0 0 
        0 1 1 1 0 0 0 0 
        ''',
    'b2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 1 1 0 0 0 0 0 
        1 0 1 0 0 0 0 0 
        1 1 1 0 0 0 0 0 
        ''',
    'a2':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        1 1 0 0 0 0 0 0 
        ''',
    'h3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 1 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 1 
        0 0 0 0 0 0 0 0 
        ''',
    'g3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 1 1 
        0 0 0 0 0 1 0 1 
        0 0 0 0 0 1 1 1 
        0 0 0 0 0 0 0 0 
        ''',
    'f3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 1 1 0 
        0 0 0 0 1 0 1 0 
        0 0 0 0 1 1 1 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 1 1 0 0 
        0 0 0 1 0 1 0 0 
        0 0 0 1 1 1 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 1 1 0 0 0 
        0 0 1 0 1 0 0 0 
        0 0 1 1 1 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 1 1 1 0 0 0 0 
        0 1 0 1 0 0 0 0 
        0 1 1 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 1 1 0 0 0 0 0 
        1 0 1 0 0 0 0 0 
        1 1 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a3':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        1 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 1 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'g4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 1 1 
        0 0 0 0 0 1 0 1 
        0 0 0 0 0 1 1 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 1 1 0 
        0 0 0 0 1 0 1 0 
        0 0 0 0 1 1 1 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 1 1 0 0 
        0 0 0 1 0 1 0 0 
        0 0 0 1 1 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 1 1 0 0 0 
        0 0 1 0 1 0 0 0 
        0 0 1 1 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 1 1 1 0 0 0 0 
        0 1 0 1 0 0 0 0 
        0 1 1 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 1 1 0 0 0 0 0 
        1 0 1 0 0 0 0 0 
        1 1 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a4':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        1 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 1 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'g5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 1 1 
        0 0 0 0 0 1 0 1 
        0 0 0 0 0 1 1 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 1 1 0 
        0 0 0 0 1 0 1 0 
        0 0 0 0 1 1 1 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 1 1 1 0 0 
        0 0 0 1 0 1 0 0 
        0 0 0 1 1 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 1 1 1 0 0 0 
        0 0 1 0 1 0 0 0 
        0 0 1 1 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 1 1 1 0 0 0 0 
        0 1 0 1 0 0 0 0 
        0 1 1 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 1 1 0 0 0 0 0 
        1 0 1 0 0 0 0 0 
        1 1 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a5':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        1 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        1 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h6':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 1 1 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'g6':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 1 1 1 
        0 0 0 0 0 1 0 1 
        0 0 0 0 0 1 1 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f6':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 0 1 1 1 0 
        0 0 0 0 1 0 1 0 
        0 0 0 0 1 1 1 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e6':
        '''
        0 0 0 0 0 0 0 0 
        0 0 0 1 1 1 0 0 
        0 0 0 1 0 1 0 0 
        0 0 0 1 1 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd6':
        '''
        0 0 0 0 0 0 0 0 
        0 0 1 1 1 0 0 0 
        0 0 1 0 1 0 0 0 
        0 0 1 1 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c6':
        '''
        0 0 0 0 0 0 0 0 
        0 1 1 1 0 0 0 0 
        0 1 0 1 0 0 0 0 
        0 1 1 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b6':
        '''
        0 0 0 0 0 0 0 0 
        1 1 1 0 0 0 0 0 
        1 0 1 0 0 0 0 0 
        1 1 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a6':
        '''
        0 0 0 0 0 0 0 0 
        1 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        1 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h7':
        '''
        0 0 0 0 0 0 1 1 
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'g7':
        '''
        0 0 0 0 0 1 1 1 
        0 0 0 0 0 1 0 1 
        0 0 0 0 0 1 1 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f7':
        '''
        0 0 0 0 1 1 1 0 
        0 0 0 0 1 0 1 0 
        0 0 0 0 1 1 1 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e7':
        '''
        0 0 0 1 1 1 0 0 
        0 0 0 1 0 1 0 0 
        0 0 0 1 1 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd7':
        '''
        0 0 1 1 1 0 0 0 
        0 0 1 0 1 0 0 0 
        0 0 1 1 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c7':
        '''
        0 1 1 1 0 0 0 0 
        0 1 0 1 0 0 0 0 
        0 1 1 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b7':
        '''
        1 1 1 0 0 0 0 0 
        1 0 1 0 0 0 0 0 
        1 1 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a7':
        '''
        1 1 0 0 0 0 0 0 
        0 1 0 0 0 0 0 0 
        1 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'h8':
        '''
        0 0 0 0 0 0 1 0 
        0 0 0 0 0 0 1 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'g8':
        '''
        0 0 0 0 0 1 0 1 
        0 0 0 0 0 1 1 1 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'f8':
        '''
        0 0 0 0 1 0 1 0 
        0 0 0 0 1 1 1 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'e8':
        '''
        0 0 0 1 0 1 0 0 
        0 0 0 1 1 1 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'd8':
        '''
        0 0 1 0 1 0 0 0 
        0 0 1 1 1 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'c8':
        '''
        0 1 0 1 0 0 0 0 
        0 1 1 1 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'b8':
        '''
        1 0 1 0 0 0 0 0 
        1 1 1 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
    'a8':
        '''
        0 1 0 0 0 0 0 0 
        1 1 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        0 0 0 0 0 0 0 0 
        ''',
}

white_king_castle = {
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

black_king_castle = {}
