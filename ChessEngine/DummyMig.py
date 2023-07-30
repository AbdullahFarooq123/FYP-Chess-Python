import os

dummy_pre = '''pawn_attack_maps = []

king_attack_maps = []

knight_attack_maps = []

square_bitmask = []

directional_rays = []

bishop_attacks = []
bishop_attacks_table = []
bishop_magic_number = []
bishop_attack_count = []

rook_attacks = []
rook_attacks_table = []
rook_magic_number = []
rook_attack_count = []'''
with open(f'{os.getcwd()}\\src\\Root\\PreCalculationsData.py', 'w') as data_file:
    data_file.write(dummy_pre)
