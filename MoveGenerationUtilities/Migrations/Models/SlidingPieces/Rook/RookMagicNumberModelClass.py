from enum import Enum
from sqlite3 import Cursor

from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.Migrations.BaseModel import BaseModelClass
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import rook_magic_number


class RookMagicNumberModelClass(BaseModelClass):
    class Columns(Enum):
        Id = 'Id'
        MagicNumber = 'MagicNumber'

    table_name = 'RookMagicNumber'
    create_query = f'''CREATE TABLE {table_name} 
                                                (
                                                    {Columns.Id.value} 
                                                        INTEGER 
                                                        PRIMARY KEY
                                                        ASC ON CONFLICT ROLLBACK 
                                                        AUTOINCREMENT
                                                        UNIQUE ON CONFLICT ROLLBACK 
                                                        NOT NULL ON CONFLICT ROLLBACK,
                                                    {Columns.MagicNumber.value}   
                                                        TEXT 
                                                        NOT NULL ON CONFLICT ROLLBACK
                                                );'''

    def __init__(self, con_cursor: Cursor):
        super().__init__(self.table_name, self.create_query, con_cursor)
        self.con_cursor: Cursor = con_cursor

    def init_table(self):
        for position in list(Positions)[:-1]:
            magic_number = rook_magic_number[position.value]
            query = f'''
                    INSERT INTO {self.table_name} 
                    (
                        {self.Columns.Id.value}, 
                        {self.Columns.MagicNumber.value}
                    )
                    VALUES 
                    (
                        {position.value}, 
                        "{magic_number}"
                    )
                    '''
            self.con_cursor.execute(query)
