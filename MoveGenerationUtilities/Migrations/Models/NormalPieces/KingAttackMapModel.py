from enum import Enum
from sqlite3 import Cursor

from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions
from MoveGenerationUtilities.Migrations.BaseModel import BaseModelClass
from MoveGenerationUtilities.Migrations.Models.GameDependencies.PositionModel import PositionModelClass
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import king_attack_maps


class KingAttackMapModelClass(BaseModelClass):
    class Columns(Enum):
        Id = 'Id'
        Position = 'Position'
        AttackMap = 'AttackMap'

    table_name = 'KingAttackMaps'
    create_query = f'''CREATE TABLE {table_name} 
                                                (
                                                    {Columns.Id.value}       
                                                        INTEGER 
                                                        PRIMARY KEY 
                                                        ASC ON CONFLICT ROLLBACK 
                                                        AUTOINCREMENT
                                                        NOT NULL ON CONFLICT ROLLBACK
                                                        UNIQUE ON CONFLICT ROLLBACK,
                                                    {Columns.Position.value} 
                                                        TEXT    
                                                        REFERENCES {PositionModelClass.table_name} 
                                                            ({PositionModelClass.Columns.Position.value}) 
                                                        NOT NULL ON CONFLICT ROLLBACK,
                                                    {Columns.AttackMap.value}    
                                                        TEXT 
                                                        NOT NULL ON CONFLICT ROLLBACK 
                                                );'''

    def __init__(self, con_cursor: Cursor):
        super().__init__(self.table_name, self.create_query, con_cursor)
        self.con_cursor: Cursor = con_cursor

    def init_table(self):
        for position in list(Positions)[:-1]:
            attack = king_attack_maps[position.value]
            query = f'''
                INSERT INTO {KingAttackMapModelClass.table_name} 
                    (
                        {self.Columns.Position.value}, 
                        {self.Columns.AttackMap.value}
                    ) 
                VALUES 
                    (
                        "{position.name}", 
                        "{attack}"
                    )
                '''
            self.con_cursor.executescript(query)
