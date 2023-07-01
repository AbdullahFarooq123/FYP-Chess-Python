import sqlite3
from sqlite3 import Cursor

from Migrations.BaseModel import BaseModelClass
from Migrations.Models.BishopAttackCountModel import BishopAttackCountModelClass
from Migrations.Models.BishopAttacksModel import BishopAttacksModelClass
from Migrations.Models.BishopAttacksTableModel import BishopAttacksTableModelClass
from Migrations.Models.BishopMagicNumberModel import BishopMagicNumberModelClass
from Migrations.Models.DirectionalRaysModel import DirectionalRaysModelClass
from Migrations.Models.DirectionsModel import DirectionsModelClass
from Migrations.Models.KingAttackMapModel import KingAttackMapModelClass
from Migrations.Models.KnightAttackMapModel import KnightAttackMapModelClass
from Migrations.Models.PawnAttackMapModel import PawnAttackMapModelClass
from Migrations.Models.PlayerSideModelClass import PlayerSideModelClass
from Migrations.Models.PositionsModel import PositionsModelClass
from Migrations.Models.RookAttackCountModel import RookAttackCountModelClass
from Migrations.Models.RookAttacksModel import RookAttacksModelClass
from Migrations.Models.RookAttacksTableModelClass import RookAttacksTableModelClass
from Migrations.Models.RookMagicNumberModelClass import RookMagicNumberModelClass
from Migrations.Models.SquareBitmaskModel import SquareBitmaskModelClass


class Migrations:
    def __init__(self):
        connection = sqlite3.connect('ChessDb')
        cursor: Cursor = connection.cursor()
        self.player_side_model: BaseModelClass = PlayerSideModelClass(cursor)
        self.positions_model: BaseModelClass = PositionsModelClass(cursor)
        self.bitmask_model: BaseModelClass = SquareBitmaskModelClass(cursor)
        self.directions_model: BaseModelClass = DirectionsModelClass(cursor)
        self.directional_rays_model: BaseModelClass = DirectionalRaysModelClass(cursor)
        self.pawn_attack_model: BaseModelClass = PawnAttackMapModelClass(cursor)
        self.knight_attack_model: BaseModelClass = KnightAttackMapModelClass(cursor)
        self.king_attack_model: BaseModelClass = KingAttackMapModelClass(cursor)
        self.bishop_magic_number_model: BaseModelClass = BishopMagicNumberModelClass(cursor)
        self.bishop_attack_count_model: BaseModelClass = BishopAttackCountModelClass(cursor)
        self.bishop_attack_model: BaseModelClass = BishopAttacksModelClass(cursor)
        self.bishop_attack_table_model: BaseModelClass = BishopAttacksTableModelClass(cursor)
        self.rook_magic_number_model: BaseModelClass = RookMagicNumberModelClass(cursor)
        self.rook_attack_count_model: BaseModelClass = RookAttackCountModelClass(cursor)
        self.rook_attacks_model: BaseModelClass = RookAttacksModelClass(cursor)
        self.rook_attack_table_model: BaseModelClass = RookAttacksTableModelClass(cursor)

    def run_migrations(self):
        self.player_side_model.run_migration()
        self.positions_model.run_migration()
        self.directions_model.run_migration()
        self.directional_rays_model.run_migration()
        self.bitmask_model.run_migration()
        self.pawn_attack_model.run_migration()
        self.knight_attack_model.run_migration()
        self.king_attack_model.run_migration()
        self.bishop_magic_number_model.run_migration()
        self.bishop_attack_count_model.run_migration()
        self.bishop_attack_model.run_migration()
        self.bishop_attack_table_model.run_migration()
        self.rook_magic_number_model.run_migration()
        self.rook_attack_count_model.run_migration()
        self.rook_attacks_model.run_migration()
        self.rook_attack_table_model.run_migration()

    def run_select(self):
        self.player_side_model.print_select()
        self.positions_model.print_select()
        self.directions_model.print_select()
        self.directional_rays_model.print_select()
        self.bitmask_model.print_select()
        self.pawn_attack_model.print_select()
        self.knight_attack_model.print_select()
        self.king_attack_model.print_select()
        self.bishop_magic_number_model.print_select()
        self.bishop_attack_count_model.print_select()
        self.bishop_attack_model.print_select()
        self.bishop_attack_table_model.print_select()
        self.rook_magic_number_model.print_select()
        self.rook_attack_count_model.print_select()
        self.rook_attacks_model.print_select()
        self.rook_attack_table_model.print_select()
