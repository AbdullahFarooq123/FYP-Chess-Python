from enum import Enum
from sqlite3 import Cursor

from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from Migrations.BaseModel import BaseModelClass
from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.SlidingPieces.Rook import \
    get_rook_magic_index_and_attack


class RookAttacksTableModelClass(BaseModelClass):
    class Columns(Enum):
        Id = 'Id'
        Position = 'Position'
        MagicIndex = 'MagicIndex'
        Value = 'Value'

    table_name = 'RookAttacksTable'
    create_query = f'''CREATE TABLE {table_name} (
                                                        {Columns.Id.value}        INTEGER PRIMARY KEY ASC ON CONFLICT ROLLBACK AUTOINCREMENT
                                                                          UNIQUE
                                                                          NOT NULL,
                                                        {Columns.Position.value}  TEXT    REFERENCES Positions (Id) 
                                                                          NOT NULL,
                                                        {Columns.MagicIndex.value} INTEGER NOT NULL,
                                                        {Columns.Value.value}     INTEGER NOT NULL
                                                    );'''

    def __init__(self, con_cursor: Cursor):
        super().__init__(self.table_name, self.create_query, con_cursor)
        self.con_cursor: Cursor = con_cursor

    def init_table(self):
        for position in list(Positions)[:-1]:
            for magic_index, attack in get_rook_magic_index_and_attack(position=position):
                query = f'''
                            INSERT INTO {self.table_name} 
                                ({self.Columns.Position.value}, {self.Columns.MagicIndex.value}, {self.Columns.Value.value}) 
                            VALUES 
                                ("{position.name}", {magic_index}, {attack})
                        '''
                self.con_cursor.executescript(query)
