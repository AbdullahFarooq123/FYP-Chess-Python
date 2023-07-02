from enum import Enum
from sqlite3 import Cursor

from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide
from Migrations.BaseModel import BaseModelClass
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import pawn_attack_maps


class PawnAttackMapModelClass(BaseModelClass):
    class Columns(Enum):
        Id = 'Id'
        PlayerSide = 'PlayerSide'
        Position = 'Position'
        Value = 'Value'

    table_name = 'PawnAttackMaps'
    create_query = f'''CREATE TABLE {table_name} (
                                                    {Columns.Id.value}             INTEGER PRIMARY KEY ASC ON CONFLICT ROLLBACK AUTOINCREMENT
                                                                           UNIQUE ON CONFLICT ROLLBACK
                                                                           NOT NULL ON CONFLICT ROLLBACK,
                                                    {Columns.PlayerSide.value}     TEXT    REFERENCES PlayerSides (PlayerSide) 
                                                                           NOT NULL,
                                                    {Columns.Position.value} TEXT    REFERENCES Positions (Position) 
                                                                           NOT NULL ON CONFLICT ROLLBACK,
                                                    {Columns.Value.value}          INTEGER NOT NULL
                                                );'''

    def __init__(self, con_cursor: Cursor):
        super().__init__(self.table_name, self.create_query, con_cursor)
        self.con_cursor: Cursor = con_cursor

    def init_table(self):
        for side in list(PlayerSide)[:-1]:
            for position in list(Positions)[:-1]:
                attack = pawn_attack_maps[side.value][position.value]
                query = f'''
                    INSERT INTO {PawnAttackMapModelClass.table_name} 
                        ({self.Columns.PlayerSide.value}, {self.Columns.Position.value}, {self.Columns.Value.value}) 
                    VALUES 
                        ("{side.name}", "{position.name}", {attack})
                    '''
                self.con_cursor.executescript(query)
