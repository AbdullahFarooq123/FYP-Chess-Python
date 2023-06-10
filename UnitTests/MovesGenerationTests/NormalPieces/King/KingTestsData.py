from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PieceDependency.PieceNameDependency import PieceName

# King's Move Tests 

white_king_test_data = {


# Normal King Move
# 8 r  .  .  .  k  .  .  .  
# 7 .  .  .  .  .  .  .  .  
# 6 .  .  .  .  .  .  .  .  
# 5 .  .  .  .  .  .  .  .  
# 4 .  .  .  .  .  .  .  .  
# 3 .  .  .  .  .  .  .  .  
# 2 .  .  .  .  .  .  .  .
# 1 .  .  .  .  K  .  .  .
#   a  b  c  d  e  f  g  h

 'r3k3/8/8/8/8/8/8/4K3 w - - 0 1':[
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
       
    ],

# 8 .  .  .  .  k  .  .  .  
# 7 .  .  .  .  .  .  .  .  
# 6 .  .  .  .  .  .  .  .  
# 5 .  .  .  .  .  .  .  .  
# 4 .  .  .  .  .  .  .  .  
# 3 .  .  .  .  .  .  .  .  
# 2 .  .  .  .  .  .  .  .
# 1 R  .  .  .  K  .  .  R

#   a  b  c  d  e  f  g  h

    '4k3/8/8/8/8/8/8/R3K2R w KQ - 0 1':[
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

    '4k3/8/8/8/8/8/4P3/4K3 w - - 0 1':[
     
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

    '4k3/8/3r4/8/6b1/8/8/4K3 w - - 0 1':[
     
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
# 1 R .  .  .  K  .  .  .
#   a  b  c  d  e  f  g  h

    '4k3/8/3r1r2/8/6b1/8/8/R3K3 w - - 0 1':[],


# 8 .  .  .  .  k  .  .  .  
# 7 .  .  .  .  .  .  .  .  
# 6 .  .  .  .  .  .  .  .  
# 5 .  .  .  .  .  .  .  .  
# 4 .  .  .  .  .  .  .  .  
# 3 .  .  .  .  K  .  .  .  
# 2 .  .  .  .  .  .  .  .
# 1 R  .  .  .  .  .  .  .
#   a  b  c  d  e  f  g  h

 'r3k3/8/8/8/8/8/8/4K3 w - - 0 1':[
          {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.e2,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.d2,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.f2,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
       
          {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.d3,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.f3,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
            {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.e4,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.d4,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e3,
            'TARGET_SQUARE': Positions.f4,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
       
    ], 
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

 '4k3/8/8/3r4/8/8/5b2/R3K3 w - - 0 1':[
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

 '4k3/8/8/3r1r2/8/8/5b2/R3K3 w - - 0 1':[
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

 '4k3/8/8/3r3b/8/8/4K3/r7 w - - 0 1':[
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





black_king_test_data = {


# Normal King Move
# 8 r  .  .  .  k  .  .  .  
# 7 .  .  .  .  .  .  .  .  
# 6 .  .  .  .  .  .  .  .  
# 5 .  .  .  .  .  .  .  .  
# 4 .  .  .  .  .  .  .  .  
# 3 .  .  .  .  .  .  .  .  
# 2 .  .  .  .  .  .  .  .
# 1 .  .  .  .  K  .  .  .
#   a  b  c  d  e  f  g  h

 'r3k3/8/8/8/8/8/8/4K3 b - - 0 1':[
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.e7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.f7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
       
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.d8,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.d7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
       
    ],

# 8 r  .  .  .  k  .  .  r  
# 7 .  .  .  .  .  .  .  .  
# 6 .  .  .  .  .  .  .  .  
# 5 .  .  .  .  .  .  .  .  
# 4 .  .  .  .  .  .  .  .  
# 3 .  .  .  .  .  .  .  .  
# 2 .  .  .  .  .  .  .  .
# 1 .  .  .  .  K  .  .  .

#   a  b  c  d  e  f  g  h

    'r3k2r/8/8/8/8/8/8/4K3 b kq - 0 1':[
         {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.e7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.f7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
       
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.d8,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.d7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
       

        # # Queen side Castling
        # {
        #     'SOURCE_SQUARE': Positions.e8,
        #     'TARGET_SQUARE': Positions.c8,
        #     'PIECE_NAME': PieceName.KING,
        #     'PROMOTION_PIECE_NAME': PieceName.NONE,
        #     'CAPTURE_FLAG': False,
        #     'DOUBLE_PUSH_FLAG': False,
        #     'EN_PASSANT_FLAG': False,
        #     'CASTLE_FLAG': True,
        # },
        # # king side Castling 
        # {
        #     'SOURCE_SQUARE': Positions.e8,
        #     'TARGET_SQUARE': Positions.g8,
        #     'PIECE_NAME': PieceName.KING,
        #     'PROMOTION_PIECE_NAME': PieceName.NONE,
        #     'CAPTURE_FLAG': False,
        #     'DOUBLE_PUSH_FLAG': False,
        #     'EN_PASSANT_FLAG': False,
        #     'CASTLE_FLAG': True,
        # },
    ],

# Blocked by black piece
# 8 .  .  .  .  k  .  .  .  
# 7 .  .  .  .  p  .  .  .  
# 6 .  .  .  .  .  .  .  .  
# 5 .  .  .  .  .  .  .  .  
# 4 .  .  .  .  .  .  .  .  
# 3 .  .  .  .  .  .  .  .  
# 2 .  .  .  .  .  .  .  .
# 1 .  .  .  .  K  .  .  .

#   a  b  c  d  e  f  g  h

    '4k3/4p3/8/8/8/8/8/4K3 b - - 0 1':[
 
        {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.f7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
       
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.d8,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.d7,
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
# 6 .  .  .  R  .  .  .  .  
# 5 .  .  .  .  .  .  B  .  
# 4 .  .  .  .  .  .  .  .  
# 3 .  .  .  .  .  .  .  .  
# 2 .  .  .  .  .  .  .  .
# 1 .  .  .  .  K  .  .  .

#   a  b  c  d  e  f  g  h

    '4k3/8/3R4/6B1/8/8/8/4K3 b - - 0 1':[
     
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.f7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
      
    ],

     # All Moving squares under attack
# 8 r  .  .  .  k  .  .  .  
# 7 .  .  .  .  .  .  .  .  
# 6 .  .  .  R  .  .  .  .  
# 5 .  .  .  .  .  .  .  .  
# 4 .  .  .  .  .  R  B  .  
# 3 .  .  .  .  .  .  .  .  
# 2 .  .  .  .  .  .  .  .
# 1 . .  .  .  K  .  .  .
#   a  b  c  d  e  f  g  h

    '4k3/8/3R4/6B1/5R2/8/8/4K3 b - - 0 1':[],


# 8 r  .  .  .  .  .  .  .  
# 7 .  .  .  .  .  .  .  .  
# 6 .  .  .  .  k  .  .  .  
# 5 .  .  .  .  .  .  .  .  
# 4 .  .  .  .  .  .  .  .  
# 3 .  .  .  .  .  .  .  .  
# 2 .  .  .  .  .  .  .  .
# 1 R  .  .  .  K  .  .  .
#   a  b  c  d  e  f  g  h

 'r7/8/4k3/8/8/8/8/2B1K3 b - - 0 1':[
          {
            'SOURCE_SQUARE': Positions.e6,
            'TARGET_SQUARE': Positions.e5,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e6,
            'TARGET_SQUARE': Positions.e7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e6,
            'TARGET_SQUARE': Positions.f5,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
       
          {
            'SOURCE_SQUARE': Positions.e6,
            'TARGET_SQUARE': Positions.f6,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e6,
            'TARGET_SQUARE': Positions.f7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
            {
            'SOURCE_SQUARE': Positions.e6,
            'TARGET_SQUARE': Positions.d5,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e6,
            'TARGET_SQUARE': Positions.d6,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e6,
            'TARGET_SQUARE': Positions.d7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
       
    ], 
# Capture Move
# 8 .  .  .  r  k  .  .  .  
# 7 .  .  .  .  P  .  .  .  
# 6 .  .  .  .  .  .  .  .  
# 5 .  .  .  .  .  .  .  .  
# 4 .  .  .  .  .  .  .  .  
# 3 .  .  .  .  .  .  .  .  
# 2 .  .  .  .  .  .  .  .
# 1 .  .  B  .  K  .  .  .
#   a  b  c  d  e  f  g  h

 '3rk3/4P3/8/8/8/8/8/2B1K3 b - - 0 1':[
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.e7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': True,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.f7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.d7,
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
# 7 .  .  .  .  .  b  .  .  
# 6 .  .  .  .  .  .  .  .  
# 5 .  .  .  R  .  R  .  .  
# 4 .  .  .  .  .  .  .  .  
# 3 .  .  .  .  .  .  .  .  
# 2 .  .  .  .  .  .  .  .
# 1 R  .  .  .  K  .  .  .
#   a  b  c  d  e  f  g  h

 '4k3/5b2/8/3R1R2/8/8/8/R3K3 b - - 0 1':[
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.e7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.f8,
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
# 5 .  .  .  R  .  .  .  B  
# 4 .  .  .  .  .  .  .  .  
# 3 .  .  .  .  .  .  .  .  
# 2 .  .  .  .  K  .  .  .
# 1 r  .  .  .  .  .  .  .
#   a  b  c  d  e  f  g  h

 '4k3/8/8/3R3B/8/8/4K3/r7 b - - 0 1':[
          {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.e7,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },
        {
            'SOURCE_SQUARE': Positions.e8,
            'TARGET_SQUARE': Positions.f8,
            'PIECE_NAME': PieceName.KING,
            'PROMOTION_PIECE_NAME': PieceName.NONE,
            'CAPTURE_FLAG': False,
            'DOUBLE_PUSH_FLAG': False,
            'EN_PASSANT_FLAG': False,
            'CASTLE_FLAG': False,
        },    
        
    ], 



}