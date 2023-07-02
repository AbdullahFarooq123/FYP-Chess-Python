from enum import Enum
from sqlite3 import Cursor

from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from Migrations.BaseModel import BaseModelClass


class PositionModelClass(BaseModelClass):
    class Columns(Enum):
        Id = 'Id'
        Position = 'Position'

    table_name = 'Positions'
    create_query = f'''CREATE TABLE {table_name} (
                                                    {Columns.Id.value}       INTEGER PRIMARY KEY ASC ON CONFLICT ROLLBACK AUTOINCREMENT
                                                                     UNIQUE ON CONFLICT ROLLBACK
                                                                     NOT NULL ON CONFLICT ROLLBACK,
                                                    {Columns.Position.value} TEXT    UNIQUE ON CONFLICT ROLLBACK
                                                                     NOT NULL ON CONFLICT ROLLBACK
                                                );'''

    def __init__(self, con_cursor: Cursor):
        super().__init__(self.table_name, self.create_query, con_cursor)
        self.con_cursor: Cursor = con_cursor

    def init_table(self):
        for position in Positions:
            query = f'''
                INSERT INTO {PositionModelClass.table_name} 
                    ({self.Columns.Position.value}) 
                VALUES 
                    ("{position.name}")
                '''
            self.con_cursor.executescript(query)
