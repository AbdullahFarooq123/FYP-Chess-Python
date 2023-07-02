from enum import Enum
from sqlite3 import Cursor

from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from Migrations.BaseModel import BaseModelClass
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import bishop_magic_number


class BishopMagicNumberModelClass(BaseModelClass):
    class Columns(Enum):
        Id = 'Id'
        Value = 'Value'

    table_name = 'BishopMagicNumber'
    create_query = f'''CREATE TABLE {table_name} (
                                                        {Columns.Id.value} INTEGER PRIMARY KEY
                                                                        UNIQUE
                                                                        NOT NULL,
                                                        {Columns.Value.value}   INTEGER NOT NULL
                                                    );'''

    def __init__(self, con_cursor: Cursor):
        super().__init__(self.table_name, self.create_query, con_cursor)
        self.con_cursor: Cursor = con_cursor

    def init_table(self):
        for position in list(Positions)[:-1]:
            magic_number = bishop_magic_number[position.value]
            query = f'''
                    INSERT INTO {self.table_name} 
                        ({self.Columns.Id.value}, {self.Columns.Value.value})
                    VALUES 
                        ({position.value}, {magic_number})
                    '''
            self.con_cursor.execute(query)
