from enum import Enum
from sqlite3 import Cursor

from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from MoveGenerationUtilities.Migrations.BaseModel import BaseModelClass


class DirectionsModelClass(BaseModelClass):
    class Columns(Enum):
        Id = 'Id'
        Direction = 'Direction'

    table_name = 'Directions'
    create_query = f'''CREATE TABLE {table_name} 
                                                (
                                                    {Columns.Id.value}        
                                                        INTEGER 
                                                        PRIMARY KEY 
                                                        ASC ON CONFLICT ROLLBACK 
                                                        AUTOINCREMENT
                                                        UNIQUE ON CONFLICT ROLLBACK 
                                                        NOT NULL ON CONFLICT ROLLBACK,
                                                    {Columns.Direction.value} 
                                                        TEXT    
                                                        NOT NULL ON CONFLICT ROLLBACK 
                                                        UNIQUE ON CONFLICT ROLLBACK 
                                                );'''

    def __init__(self, con_cursor: Cursor):
        super().__init__(self.table_name, self.create_query, con_cursor)
        self.con_cursor: Cursor = con_cursor

    def init_table(self):
        for direction in SpecificDirections:
            query = f'''
            INSERT INTO {DirectionsModelClass.table_name} 
            (
                {self.Columns.Direction.value}
            ) 
            VALUES 
            (
                "{direction.name}"
            )
            '''
            self.con_cursor.executescript(query)
