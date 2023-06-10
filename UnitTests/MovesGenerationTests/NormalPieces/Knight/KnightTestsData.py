from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName

# Bishop Tests

white_knight_test_data = {
    
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
    '3qk3/8/8/8/8/2N5/8/4K1N1 w - - 1 1':[
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
    '3qk3/8/8/8/1p6/6r1/N4K2/2B4N w - - 1 1':[
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
    '3qk3/8/8/8/8/8/4K1r1/7N w - - 1 1':[
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
    '3qk3/8/8/4N3/8/8/1N2K1r1/8 w - - 1 1':[
        
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
    '3qk3/8/8/7b/5N2/8/4K3/8 w - - 1 1':[
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

    '3qk3/8/8/8/8/8/2K1N2r/8 b - - 1 1':[],

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

    '3qk3/8/8/8/b7/8/2N5/3K4 w - - 1 1':[],
    
}

black_knight_test_data = {

       # normal move
    # 8	.  .  .  .  k  .  n  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  n  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	R  .  .  K  .  .  .  .
    # 	a  b  c  d  e  f  g  h
    '4k1n1/8/2n5/8/8/8/8/R2K4 b - - 1 1':[

       {
            'SOURCE_SQUARE': Positions.c6,
            'TARGET_SQUARE': Positions.a5,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.c6,
            'TARGET_SQUARE': Positions.a7,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.c6,
            'TARGET_SQUARE': Positions.b4,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.c6,
            'TARGET_SQUARE': Positions.b8,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.c6,
            'TARGET_SQUARE': Positions.d4,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.c6,
            'TARGET_SQUARE': Positions.d8,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.c6,
            'TARGET_SQUARE': Positions.e5,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.c6,
            'TARGET_SQUARE': Positions.e7,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.g8,
            'TARGET_SQUARE': Positions.e7,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.g8,
            'TARGET_SQUARE': Positions.f6,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
         {
            'SOURCE_SQUARE': Positions.g8,
            'TARGET_SQUARE': Positions.h6,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        
    ],

    # capture move
    # 8	.  .  .  .  .  .  n  .
    # 7	n  .  .  .  k  .  .  .
    # 6	.  .  .  .  .  .  .  P
    # 5	.  P  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	R  .  .  K  .  .  .  .
    # 	a  b  c  d  e  f  g  h
    '6n1/n3k3/7P/1P6/8/8/8/R2K4 b - - 1 1':[
        {
            'SOURCE_SQUARE': Positions.a7,
            'TARGET_SQUARE': Positions.b5,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

          {
            'SOURCE_SQUARE': Positions.g8,
            'TARGET_SQUARE': Positions.h6,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.g8,
            'TARGET_SQUARE': Positions.f6,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.a7,
            'TARGET_SQUARE': Positions.c6,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

        {
            'SOURCE_SQUARE': Positions.a7,
            'TARGET_SQUARE': Positions.c8,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],

     # king in check 
    # 8	k  .  .  .  .  .  n  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	R  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  K  .  .  .  .
    # 	a  b  c  d  e  f  g  h
    'k5n1/8/8/8/8/R7/8/3K4 b - - 1 1':[],
    
    # king in check 
    # 8	k  .  .  .  .  .  .  .
    # 7	.  .  n  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	R  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  K  .  .  .  .
    # 	a  b  c  d  e  f  g  h
    'k7/2n5/8/8/8/R7/8/3K4 b - - 1 1':[
        {
            'SOURCE_SQUARE': Positions.c7,
            'TARGET_SQUARE': Positions.a6,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # king in check 
    # 8	k  .  .  .  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  n  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  B  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  K  .  .  .  .
    # 	a  b  c  d  e  f  g  h
    'k7/8/3n4/8/4B3/8/8/3K4 b - - 1 1':[
         {
            'SOURCE_SQUARE': Positions.d6,
            'TARGET_SQUARE': Positions.b7,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d6,
            'TARGET_SQUARE': Positions.e4,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],


    # pin check
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  n  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  R  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  K  .  .  .  .
    # 	a  b  c  d  e  f  g  h

    '3k4/8/3n4/8/3R4/8/8/3K4 b - - 1 1':[],


    # pin check
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  n  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  B
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  N  .
    # 1	.  .  .  K  .  .  .  .
    # 	a  b  c  d  e  f  g  h

    '3k4/8/5n2/8/7B/8/6n1/3K4 b - - 1 1':[
            
        {
            'SOURCE_SQUARE': Positions.g2,
            'TARGET_SQUARE': Positions.e1,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        
        {
            'SOURCE_SQUARE': Positions.g2,
            'TARGET_SQUARE': Positions.e3,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

        {
            'SOURCE_SQUARE': Positions.g2,
            'TARGET_SQUARE': Positions.f4,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

        {
            'SOURCE_SQUARE': Positions.g2,
            'TARGET_SQUARE': Positions.h4,
            'PIECE_NAME': PieceName.KNIGHT,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],



}