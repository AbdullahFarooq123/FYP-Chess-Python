from enum import Enum
from sqlite3 import Cursor

from DebugUtilities.GameDependency.PlayerDependency.PlayerSideDependency import PlayerSide
from Migrations.BaseModel import BaseModelClass


class PlayerSideModelClass(BaseModelClass):
    class Columns(Enum):
        Id = 'Id'
        PlayerSide = 'PlayerSide'

    table_name = 'PlayerSides'
    create_query = f'''CREATE TABLE {table_name} 
                                                (
                                                    {Columns.Id.value}         
                                                        INTEGER 
                                                        PRIMARY KEY 
                                                        ASC ON CONFLICT ROLLBACK 
                                                        AUTOINCREMENT
                                                        UNIQUE ON CONFLICT ROLLBACK
                                                        NOT NULL ON CONFLICT ROLLBACK,
                                                    {Columns.PlayerSide.value} 
                                                        TEXT    
                                                        UNIQUE ON CONFLICT ROLLBACK
                                                        NOT NULL ON CONFLICT ROLLBACK
                                                );'''

    def __init__(self, con_cursor: Cursor):
        super().__init__(self.table_name, self.create_query, con_cursor)
        self.con_cursor: Cursor = con_cursor

    def init_table(self):
        for side in PlayerSide:
            query = f'''
                INSERT INTO {PlayerSideModelClass.table_name} 
                (
                    {self.Columns.PlayerSide.value}
                ) 
                VALUES 
                (
                    "{side.name}"
                )
                '''
            self.con_cursor.executescript(query)
