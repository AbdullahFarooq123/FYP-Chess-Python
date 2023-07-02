from enum import Enum
from sqlite3 import Cursor

from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from Migrations.BaseModel import BaseModelClass
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import directional_rays


class DirectionalRaysModelClass(BaseModelClass):
    class Columns(Enum):
        Id = 'Id'
        Direction = 'Direction'
        Position = 'Position'
        Value = 'Value'

    table_name = 'DirectionalRays'
    create_query = f'''CREATE TABLE {table_name} (
                                                        {Columns.Id.value}        INTEGER PRIMARY KEY ASC ON CONFLICT ROLLBACK AUTOINCREMENT
                                                                          NOT NULL,
                                                        {Columns.Direction.value} TEXT    NOT NULL ON CONFLICT ROLLBACK
                                                                          REFERENCES DirectionalRays (Direction),
                                                        {Columns.Position.value}  TEXT    REFERENCES Positions (Id) 
                                                                          NOT NULL,
                                                        {Columns.Value.value}     INTEGER NOT NULL ON CONFLICT ROLLBACK
                                                    );'''

    def __init__(self, con_cursor: Cursor):
        super().__init__(self.table_name, self.create_query, con_cursor)
        self.con_cursor: Cursor = con_cursor

    def init_table(self):
        for direction in list(SpecificDirections)[:8]:
            for position in list(Positions)[:-1]:
                ray = directional_rays[direction.value][position.value]
                query = f'''
                            INSERT INTO {DirectionalRaysModelClass.table_name} 
                                ({self.Columns.Direction.value}, {self.Columns.Position.value}, {self.Columns.Value.value}) 
                            VALUES 
                                ("{direction.name}", "{position.name}", {ray})
                        '''
                self.con_cursor.executescript(query)
