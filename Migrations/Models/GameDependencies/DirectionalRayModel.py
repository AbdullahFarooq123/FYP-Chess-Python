from enum import Enum
from sqlite3 import Cursor

from DebugUtilities.GameDependency.BoardDependency.DirectionalDependency.SpecificDirectionDependency import \
    SpecificDirections
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from Migrations.BaseModel import BaseModelClass
from Migrations.Models.GameDependencies.DirectionModel import DirectionsModelClass
from Migrations.Models.GameDependencies.PositionModel import PositionModelClass
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import directional_rays


class DirectionalRayModelClass(BaseModelClass):
    class Columns(Enum):
        Id = 'Id'
        Direction = 'Direction'
        Position = 'Position'
        Ray = 'Ray'

    table_name = 'DirectionalRay'
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
                                                        REFERENCES {DirectionsModelClass.table_name} 
                                                            ({DirectionsModelClass.Columns.Direction.value}),
                                                    {Columns.Position.value}  
                                                        TEXT    
                                                        REFERENCES {PositionModelClass.table_name} 
                                                            ({PositionModelClass.Columns.Position.value}) 
                                                        NOT NULL ON CONFLICT ROLLBACK,
                                                    {Columns.Ray.value}     
                                                        INTEGER 
                                                        NOT NULL ON CONFLICT ROLLBACK
                                                );'''

    def __init__(self, con_cursor: Cursor):
        super().__init__(self.table_name, self.create_query, con_cursor)
        self.con_cursor: Cursor = con_cursor

    def init_table(self):
        for direction in list(SpecificDirections)[:8]:
            for position in list(Positions)[:-1]:
                ray = directional_rays[direction.value][position.value]
                query = f'''
                            INSERT INTO {DirectionalRayModelClass.table_name} 
                            (
                                {self.Columns.Direction.value}, 
                                {self.Columns.Position.value}, 
                                {self.Columns.Ray.value}
                            ) 
                            VALUES 
                            (
                                "{direction.name}", 
                                "{position.name}", 
                                 {ray}
                            )
                        '''
                self.con_cursor.executescript(query)
