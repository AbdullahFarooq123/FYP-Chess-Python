from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName

# Rook tests

white_rook_test_data = {

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

    '3k4/8/4P3/8/8/4R3/8/4K3 w - - 0 1':[
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

    '3k4/8/8/r7/8/R3n3/8/R2QK3 w - - 0 1':[

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
    '3k4/8/8/8/8/R4n2/8/R2QK3 w - - 0 1':[
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
    '3k4/8/8/8/8/6b1/6R1/3QK3 w - - 0 1':[
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

    '4k3/8/8/8/7b/8/5R2/4K3 w - - 0 1':[],

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

    '4k3/8/8/8/7b/3n4/3R1R2/4K3 w - - 0 1':[
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

    '4k3/8/8/8/7b/8/1P3R2/1R2K3 w - - 0 1':[
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

black_rook_test_data = {
    # normal move
    # 8	.  .  r  .  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '2r1k3/8/8/8/8/8/8/4K3 b - - 0 1':[
            {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.a8,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
              {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.b8,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
              {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.d8,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
              {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.c7,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
              {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.c6,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
              {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.c5,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
              {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.c4,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
              {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.c3,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
              {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.c2,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
              {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # capture move
    # 8	.  .  r  q  k  r  .  .
    # 7	.  .  P  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  R  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  .  .  .  .
    #   a  b  c  d  e  f  g  h
    '2rqkr2/2P5/8/5R2/8/8/8/4K3 b - - 0 1':[
                  {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.a8,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
                  {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.b8,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
                  {
            'SOURCE_SQUARE': Positions.c8,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
                  {
            'SOURCE_SQUARE': Positions.f8,
            'TARGET_SQUARE': Positions.f6,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
                  {
            'SOURCE_SQUARE': Positions.f8,
            'TARGET_SQUARE': Positions.f7,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
                  {
            'SOURCE_SQUARE': Positions.f8,
            'TARGET_SQUARE': Positions.f5,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
                  {
            'SOURCE_SQUARE': Positions.f8,
            'TARGET_SQUARE': Positions.g8,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
                  {
            'SOURCE_SQUARE': Positions.f8,
            'TARGET_SQUARE': Positions.h8,
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
    # 7	.  .  .  r  .  .  .  .
    # 6	.  .  B  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '4k3/3r4/2B5/8/8/8/8/4K3 b - - 0 1':[],
      # pin check
    # 8	.  .  .  .  k  .  r  .
    # 7	.  .  .  r  .  .  p  .
    # 6	.  .  B  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '4k1r1/3r2p1/2B5/8/8/8/8/4K3 b - - 0 1':[
        {
            'SOURCE_SQUARE': Positions.g8,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.g8,
            'TARGET_SQUARE': Positions.h8,
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
    # 7	.  .  .  r  .  .  N  .
    # 6	.  .  B  .  .  r  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '4k3/3r2N1/2B2r2/8/8/8/8/4K3 b - - 0 1':[],

    # king in check
    # 8	.  .  .  .  k  .  .  .
    # 7	.  .  .  r  .  .  N  .
    # 6	.  .  .  .  .  r  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '4k3/3r2N1/5r2/8/8/8/8/4K3 b - - 0 1':[
        {
            'SOURCE_SQUARE': Positions.d7,
            'TARGET_SQUARE': Positions.g7,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    
    # king in check
    # 8	.  .  .  .  k  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  r  .  .
    # 5	.  .  .  .  .  .  .  B
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '4k3/8/5r2/7B/8/8/8/4K3 b - - 0 1':[
        {
            'SOURCE_SQUARE': Positions.f6,
            'TARGET_SQUARE': Positions.f7,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f6,
            'TARGET_SQUARE': Positions.g7,
            'PIECE_NAME': PieceName.ROOK,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

}