from enum import Enum
from sqlite3 import Cursor

from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from Migrations.BaseModel import BaseModelClass
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import rook_attacks


class RookAttacksModelClass(BaseModelClass):
    class Columns(Enum):
        Id = 'Id'
        Position = 'Position'
        Value = 'Value'

    table_name = 'RookAttacks'
    create_query = f'''CREATE TABLE {table_name} (
                                        {Columns.Id.value} INTEGER PRIMARY KEY ASC ON CONFLICT ROLLBACK AUTOINCREMENT
                                                         UNIQUE
                                                         NOT NULL,
                                        {Columns.Position.value} TEXT    REFERENCES Positions (Id) 
                                                         NOT NULL,
                                        {Columns.Value.value}    INTEGER NOT NULL
                                                );'''

    def __init__(self, con_cursor: Cursor):
        super().__init__(self.table_name, self.create_query, con_cursor)
        self.con_cursor: Cursor = con_cursor

    def init_table(self):
        for position in list(Positions)[:-1]:
            ray = rook_attacks[position.value]
            query = f'''
                        INSERT INTO {self.table_name} 
                        ({self.Columns.Position.value}, {self.Columns.Value.value}) 
                        VALUES 
                        ("{position.name}", {ray})
                    '''
            self.con_cursor.executescript(query)
