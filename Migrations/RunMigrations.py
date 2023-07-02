import sqlite3
from sqlite3 import Cursor

from Migrations.BaseModel import BaseModelClass
from Migrations.Models.SlidingPieces.Bishop.BishopAttackCountModel import BishopAttackCountModelClass
from Migrations.Models.SlidingPieces.Bishop.BishopAttackExcEndsModel import BishopAttackExcEndsModelClass
from Migrations.Models.SlidingPieces.Bishop.BishopAttackTableModel import BishopAttackTableModelClass
from Migrations.Models.SlidingPieces.Bishop.BishopMagicNumberModel import BishopMagicNumberModelClass
from Migrations.Models.GameDependencies.DirectionalRayModel import DirectionalRayModelClass
from Migrations.Models.GameDependencies.DirectionModel import DirectionsModelClass
from Migrations.Models.NormalPieces.KingAttackMapModel import KingAttackMapModelClass
from Migrations.Models.NormalPieces.KnightAttackMapModel import KnightAttackMapModelClass
from Migrations.Models.NormalPieces.PawnAttackMapModel import PawnAttackMapModelClass
from Migrations.Models.GameDependencies.PlayerSideModel import PlayerSideModelClass
from Migrations.Models.GameDependencies.PositionModel import PositionModelClass
from Migrations.Models.SlidingPieces.Rook.RookAttackCountModel import RookAttackCountModelClass
from Migrations.Models.SlidingPieces.Rook.RookAttackExcEndModel import RookAttackExcEndModelClass
from Migrations.Models.SlidingPieces.Rook.RookAttackTableModelClass import RookAttacksTableModelClass
from Migrations.Models.SlidingPieces.Rook.RookMagicNumberModelClass import RookMagicNumberModelClass
from Migrations.Models.GameDependencies.SquareBitmaskModel import SquareBitmaskModelClass


class Migrations:
    def __init__(self):
        self.connection = sqlite3.connect('ChessDb')
        self.cursor: Cursor = self.connection.cursor()
        self.player_side_model: BaseModelClass = PlayerSideModelClass(self.cursor)
        self.positions_model: BaseModelClass = PositionModelClass(self.cursor)
        self.bitmask_model: BaseModelClass = SquareBitmaskModelClass(self.cursor)
        self.directions_model: BaseModelClass = DirectionsModelClass(self.cursor)
        self.directional_rays_model: BaseModelClass = DirectionalRayModelClass(self.cursor)
        self.pawn_attack_model: BaseModelClass = PawnAttackMapModelClass(self.cursor)
        self.knight_attack_model: BaseModelClass = KnightAttackMapModelClass(self.cursor)
        self.king_attack_model: BaseModelClass = KingAttackMapModelClass(self.cursor)
        self.bishop_magic_number_model: BaseModelClass = BishopMagicNumberModelClass(self.cursor)
        self.bishop_attack_count_model: BaseModelClass = BishopAttackCountModelClass(self.cursor)
        self.bishop_attack_model: BaseModelClass = BishopAttackExcEndsModelClass(self.cursor)
        self.bishop_attack_table_model: BaseModelClass = BishopAttackTableModelClass(self.cursor)
        self.rook_magic_number_model: BaseModelClass = RookMagicNumberModelClass(self.cursor)
        self.rook_attack_count_model: BaseModelClass = RookAttackCountModelClass(self.cursor)
        self.rook_attacks_model: BaseModelClass = RookAttackExcEndModelClass(self.cursor)
        self.rook_attack_table_model: BaseModelClass = RookAttacksTableModelClass(self.cursor)

    @staticmethod
    def get_cursor() -> Cursor:
        connection = sqlite3.connect('ChessDb')
        return connection.cursor()

    def run_migrations(self):
        BaseModelClass.drop_all_tables(self.cursor)
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
        self.connection.commit()

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
