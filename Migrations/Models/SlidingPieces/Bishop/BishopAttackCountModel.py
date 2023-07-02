from enum import Enum
from sqlite3 import Cursor

from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from Migrations.BaseModel import BaseModelClass
from Migrations.Models.GameDependencies.PositionModel import PositionModelClass
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import bishop_attack_count


class BishopAttackCountModelClass(BaseModelClass):
    class Columns(Enum):
        Id = 'Id'
        Position = 'Position'
        Count = 'Count'

    table_name = 'BishopAttackCount'
    create_query = f'''CREATE TABLE {table_name} 
                                                (
                                                    {Columns.Id.value} 
                                                        INTEGER 
                                                        PRIMARY KEY
                                                        ASC ON CONFLICT ROLLBACK
                                                        AUTOINCREMENT
                                                        UNIQUE ON CONFLICT ROLLBACK
                                                        NOT NULL ON CONFLICT ROLLBACK,
                                                    {Columns.Position.value} 
                                                        TEXT 
                                                        REFERENCES {PositionModelClass.table_name} 
                                                            ({PositionModelClass.Columns.Position.value}) 
                                                        NOT NULL ON CONFLICT ROLLBACK,
                                                    {Columns.Count.value} 
                                                        INTEGER 
                                                        NOT NULL ON CONFLICT ROLLBACK
                                                );'''

    def __init__(self, con_cursor: Cursor):
        super().__init__(self.table_name, self.create_query, con_cursor)
        self.con_cursor: Cursor = con_cursor

    def init_table(self):
        for position in Positions:
            attack_count = bishop_attack_count[position.value]
            query = f'''
                        INSERT INTO {self.table_name} 
                        (
                            {self.Columns.Position.value}, 
                            {self.Columns.Count.value}
                        ) 
                        VALUES 
                        (
                            "{position.name}", 
                             {attack_count}
                        )
                    '''
            self.con_cursor.executescript(query)
