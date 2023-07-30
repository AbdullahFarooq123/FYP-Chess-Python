from ChessEngine.src.Enums.PositionsEnum import Positions
from ChessEngine.src.Enums.PieceNameEnum import PieceName

white_pawn = {
    # Enpassant Check
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  P  p  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '3k4/8/8/3Pp3/8/8/8/4K3 w - e6 0 3': [
        {
            'SOURCE_SQUARE': Positions.d5,
            'TARGET_SQUARE': Positions.d6,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d5,
            'TARGET_SQUARE': Positions.e6,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': True,
            'CASTLE_FLAG': False,
        },

    ],
    # Enpassant pin check
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  r  .  .  .  .
    # 5	.  .  .  P  p  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  K  .  .  .  .
    #
    # 	a  b  c  d  e  f  g  h
    '3k4/8/3r4/3Pp3/8/8/8/3K4 w - e6 0 3': [],

    # Capture pin check
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	b  .  .  .  .  .  .  .
    # 3	.  .  .  p  .  .  .  .
    # 2	.  .  P  .  .  .  .  .
    # 1	.  .  .  K  .  .  .  .
    #
    # 	a  b  c  d  e  f  g  h
    '3k4/8/8/8/b7/3p4/2P5/3K4 w - - 0 5': [],

    # Pawn Promotion pin check
    # 8	.  .  .  .  .  .  .  .
    # 7	.  r  .  P  .  K  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  k  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  .  .  .  .
    # 	a  b  c  d  e  f  g  h
    '8/1r1P1K2/8/8/4k3/8/8/8 w - - 0 5': [],

    # Pawn Capture and Promotion
    # 8 .  .  b  .  .  k  .  .  
    # 7 .  .  .  P  .  .  .  .
    # 6 .  .  .  .  .  .  .  .  
    # 5 .  .  .  .  .  K  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  .  .  .  
    # 1 .  .  .  .  .  .  .  .
    #   a  b  c  d  e  f  g  h
    '2b2k2/3P4/8/5K2/8/8/8/8 w - - 0 5': [

        {
            'SOURCE_SQUARE': Positions.d7,
            'TARGET_SQUARE': Positions.c8,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.BISHOP,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d7,
            'TARGET_SQUARE': Positions.c8,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.KNIGHT,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d7,
            'TARGET_SQUARE': Positions.c8,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.QUEEN,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.d7,
            'TARGET_SQUARE': Positions.c8,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.ROOK,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
    ],

    # 1 square move/Double Push pin check
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	b  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  P  .  .  .  .  .
    # 1	.  .  .  K  .  .  .  .
    # 	a  b  c  d  e  f  g  h

    '3k4/8/8/8/b7/8/2P5/3K4 w - - 0 5': [],

    # Check 1 square move, Double Push
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	P  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '3k4/8/8/8/8/8/P7/4K3 w - - 0 3': [
        {
            'SOURCE_SQUARE': Positions.a2,
            'TARGET_SQUARE': Positions.a3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.a2,
            'TARGET_SQUARE': Positions.a4,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': True,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],
    # Check 1 square move,Double Push, Capture
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  p  .  .
    # 2	.  .  .  .  P  P  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '3k4/8/8/8/8/5p2/4PP2/4K3 w - - 0 2': [
        {
            'SOURCE_SQUARE': Positions.e2,
            'TARGET_SQUARE': Positions.e3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        # check double push
        {
            'SOURCE_SQUARE': Positions.e2,
            'TARGET_SQUARE': Positions.e4,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': True,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        # check Capture
        {
            'SOURCE_SQUARE': Positions.e2,
            'TARGET_SQUARE': Positions.f3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],
    # check Pawn promotion
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  P  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '3k4/5P2/8/8/8/8/8/4K3 w - - 0 2': [
        {
            'SOURCE_SQUARE': Positions.f7,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.BISHOP,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f7,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.KNIGHT,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f7,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.QUEEN,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f7,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.ROOK,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],
    # Check Blocked piece move
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  .  .  .  .  .
    # 4	.  p  .  .  .  .  .  .
    # 3	p  .  .  .  .  .  .  .
    # 2	P  P  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '3k4/8/8/8/1p6/p7/PP6/4K3 w - - 0 3': [
        # Check capture (pawn b2=>a3)
        {
            'SOURCE_SQUARE': Positions.b2,
            'TARGET_SQUARE': Positions.a3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        # 1 square move
        {
            'SOURCE_SQUARE': Positions.b2,
            'TARGET_SQUARE': Positions.b3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        }
    ],
    # check invalid en-passant
    # 8	.  .  .  k  .  .  .  .
    # 7	.  .  .  .  .  .  .  .
    # 6	.  .  .  .  .  .  .  .
    # 5	.  .  .  P  p  .  .  .
    # 4	.  .  .  .  .  .  .  .
    # 3	.  .  .  .  .  .  .  .
    # 2	.  .  .  .  .  .  .  .
    # 1	.  .  .  .  K  .  .  .
    # 	a  b  c  d  e  f  g  h
    '3k4/8/8/3Pp3/8/8/8/4K3 w - - 0 3': [
        # only 1 square move generated (no en-passant move)
        {
            'SOURCE_SQUARE': Positions.d5,
            'TARGET_SQUARE': Positions.d6,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        }
    ],

}

black_pawn = {
    # Check 1 square move, Double Push 
    # 8 .  .  .  .  k  .  .  .
    # 7 .  .  .  .  .  .  p  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  .  .  .
    # 1 .  .  .  .  K  .  .  .
    #   a  b  c  d  e  f  g  h
    '4k3/6p1/8/8/8/8/8/4K3 b - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.g7,
            'TARGET_SQUARE': Positions.g6,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.g7,
            'TARGET_SQUARE': Positions.g5,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': True,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],

    # Check 1 Square move, Capture move

    # 8 .  .  .  .  k  .  .  .  
    # 7 .  .  .  .  .  .  .  .  
    # 6 .  .  .  .  .  .  p  .
    # 5 .  .  .  .  .  P  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  .  .  .
    # 1 .  .  .  .  K  .  .  .
    #   a  b  c  d  e  f  g  h

    '4k3/8/6p1/5P2/8/8/8/4K3 b - - 0 1': [
        {
            'SOURCE_SQUARE': Positions.g6,
            'TARGET_SQUARE': Positions.g5,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        # Check Capture 
        {
            'SOURCE_SQUARE': Positions.g6,
            'TARGET_SQUARE': Positions.f5,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],
    # Check 1 Square move, En-passant  
    # 8  .  .  .  .  k  .  .  .  
    # 7  .  .  .  .  .  .  .  .
    # 6  .  .  .  .  .  .  .  .
    # 5  .  .  .  .  .  .  .  .
    # 4  .  .  .  P  p  .  .  .
    # 3  .  .  .  .  .  .  .  .
    # 2  .  .  .  .  .  .  .  .
    # 1  .  .  .  .  K  .  .  .
    #    a  b  c  d  e  f  g  h
    '4k3/8/8/8/3Pp3/8/8/4K3 b - d3 0 2': [
        {
            'SOURCE_SQUARE': Positions.e4,
            'TARGET_SQUARE': Positions.e3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        # Check En-passant
        {
            'SOURCE_SQUARE': Positions.e4,
            'TARGET_SQUARE': Positions.d3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': True,
            'CASTLE_FLAG': False,
        },

    ],
    # Check Pawn Promotion    
    # 8 .  .  .  .  k  .  .  .  
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  p  .  .  .  .  .
    # 1 .  .  .  .  K  .  .  .
    # a  b  c  d  e  f  g  h
    '4k3/8/8/8/8/8/2p5/4K3 b - - 0 2': [
        {
            'SOURCE_SQUARE': Positions.c2,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.BISHOP,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c2,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.KNIGHT,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c2,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.QUEEN,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.c2,
            'TARGET_SQUARE': Positions.c1,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.ROOK,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],
    # Check pawn promotion when pawn is blocked
    # 8 .  .  .  .  k  .  .  .  
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  P  p  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  p  .  .  .  .  .
    # 1 .  .  P  .  K  .  .  .
    #   a  b  c  d  e  f  g  h
    '4k3/8/8/8/4Pp2/8/2p5/2P1K3 b - - 0 2': [
        # 1 square move for pawn at f4 
        {
            'SOURCE_SQUARE': Positions.f4,
            'TARGET_SQUARE': Positions.f3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],

    # En-Passant pin check
    # 8 .  .  .  .  k  .  .  .  
    # 7 .  .  .  .  .  .  .  .  
    # 6 .  .  .  .  .  .  .  .  
    # 5 .  .  .  .  .  .  .  .  
    # 4 .  .  .  P  p  .  .  .  
    # 3 .  .  .  .  R  .  .  .  
    # 2 .  .  .  .  .  .  .  .  
    # 1 .  .  .  K  .  .  .  .  
    #   a  b  c  d  e  f  g  h  

    '4k3/8/8/8/3Pp3/4R3/8/3K4 b - d3 0 3': [],

    # Capture pin check
    # 8 .  .  .  .  k  .  .  .  
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  p  .  .  .
    # 3 .  .  .  P  R  .  .  .
    # 2 .  .  .  .  .  .  .  .
    # 1 .  .  .  K  .  .  .  .
    #   a  b  c  d  e  f  g  h

    '4k3/8/8/8/4p3/3PR3/8/3K4 b - - 0 3': [],

    # Pawn Promotion pin check
    # 8 .  .  .  .  .  .  .  .  
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  K  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  k  .  p  .  R
    # 1 .  .  .  .  .  .  .  .
    #   a  b  c  d  e  f  g  h

    '8/8/8/8/1K6/8/3k1p1R/8 b - - 0 2': [],

    # Pawn promotion and Capture
    # 8 .  .  .  .  .  .  .  .  
    # 7 .  .  .  .  .  .  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  k  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  p  .  .
    # 1 .  .  .  K  .  .  B  .
    #   a  b  c  d  e  f  g  h

    '8/8/8/8/3k4/8/5p2/3K2B1 b - - 0 2': [

        {
            'SOURCE_SQUARE': Positions.f2,
            'TARGET_SQUARE': Positions.g1,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.BISHOP,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f2,
            'TARGET_SQUARE': Positions.g1,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.KNIGHT,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f2,
            'TARGET_SQUARE': Positions.g1,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.QUEEN,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.f2,
            'TARGET_SQUARE': Positions.g1,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.ROOK,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],

    # Double Push/1 square move pin check
    # 8 .  .  .  .  .  .  .  .  
    # 7 .  .  R  .  p  k  .  .
    # 6 .  .  .  .  .  .  .  .
    # 5 .  .  .  .  .  .  .  .
    # 4 .  .  .  .  .  .  .  .
    # 3 .  .  .  .  .  .  .  .
    # 2 .  .  .  .  .  .  .  .
    # 1 .  .  .  K  .  .  .  .
    #   a  b  c  d  e  f  g  h

    '8/2R1pk2/8/8/8/8/8/3K4 b - - 0 3': [],

    # Check Invalid en-passant
    # 8  .  .  .  .  .  .  .  .  
    # 7  .  .  .  .  .  k  .  .
    # 6  .  .  .  .  .  .  .  .
    # 5  .  .  .  .  .  .  .  .
    # 4  .  .  .  P  p  .  .  .
    # 3  .  .  .  .  .  .  .  .  
    # 2  .  .  .  .  .  .  .  .
    # 1  .  .  .  K  .  .  .  .
    #    a  b  c  d  e  f  g  h

    '8/5k2/8/8/3Pp3/8/8/3K4 b - - 0 5': [
        {
            'SOURCE_SQUARE': Positions.e4,
            'TARGET_SQUARE': Positions.e3,
            'PIECE_NAME': PieceName.PAWN,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },

    ],
}

pawn_attacks = {
    'BLACK': {
        'h1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'f1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'h2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 1 0 
            ''',
        'g2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 1 0 1 
            ''',
        'f2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 1 0 1 0 
            ''',
        'e2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 1 0 1 0 0 
            ''',
        'd2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 1 0 1 0 0 0 
            ''',
        'c2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 1 0 0 0 0 
            ''',
        'b2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            1 0 1 0 0 0 0 0 
            ''',
        'a2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 0 0 0 0 0 
            ''',
        'h3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 1 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 1 0 1 
            0 0 0 0 0 0 0 0 
            ''',
        'f3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 1 0 1 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 1 0 1 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 1 0 1 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 1 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            1 0 1 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'h4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 1 0 1 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'f4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 1 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 1 0 1 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 1 0 1 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 1 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            1 0 1 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'h5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 1 0 1 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'f5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 1 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 1 0 1 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 1 0 1 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 1 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            1 0 1 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'h6':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g6':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 1 0 1 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'f6':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 1 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e6':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 1 0 1 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd6':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 1 0 1 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c6':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 1 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b6':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            1 0 1 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a6':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'h7':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g7':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 1 0 1 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'f7':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 1 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e7':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 1 0 1 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd7':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 1 0 1 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c7':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 1 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b7':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            1 0 1 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a7':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'h8':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g8':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 1 0 1 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'f8':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 1 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e8':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 1 0 1 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd8':
            '''
            0 0 0 0 0 0 0 0 
            0 0 1 0 1 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c8':
            '''
            0 0 0 0 0 0 0 0 
            0 1 0 1 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b8':
            '''
            0 0 0 0 0 0 0 0 
            1 0 1 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a8':
            '''
            0 0 0 0 0 0 0 0 
            0 1 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
    },
    'WHITE': {
        'h1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 1 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 1 0 1 
            0 0 0 0 0 0 0 0 
            ''',
        'f1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 1 0 1 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 1 0 1 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 1 0 1 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 1 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            1 0 1 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a1':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'h2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 1 0 1 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'f2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 1 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 1 0 1 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 1 0 1 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 1 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            1 0 1 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a2':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'h3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 1 0 1 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'f3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 1 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 1 0 1 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 1 0 1 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 1 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            1 0 1 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a3':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'h4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 1 0 1 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'f4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 1 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 1 0 1 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 1 0 1 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 1 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            1 0 1 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a4':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'h5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 1 0 1 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'f5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 1 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 1 0 1 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 1 0 1 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 1 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            1 0 1 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a5':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 1 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'h6':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g6':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 1 0 1 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'f6':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 1 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e6':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 1 0 1 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd6':
            '''
            0 0 0 0 0 0 0 0 
            0 0 1 0 1 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c6':
            '''
            0 0 0 0 0 0 0 0 
            0 1 0 1 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b6':
            '''
            0 0 0 0 0 0 0 0 
            1 0 1 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a6':
            '''
            0 0 0 0 0 0 0 0 
            0 1 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'h7':
            '''
            0 0 0 0 0 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g7':
            '''
            0 0 0 0 0 1 0 1 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'f7':
            '''
            0 0 0 0 1 0 1 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e7':
            '''
            0 0 0 1 0 1 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd7':
            '''
            0 0 1 0 1 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c7':
            '''
            0 1 0 1 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b7':
            '''
            1 0 1 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a7':
            '''
            0 1 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'h8':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'g8':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'f8':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'e8':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'd8':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'c8':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'b8':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
        'a8':
            '''
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            0 0 0 0 0 0 0 0 
            ''',
    }
}
