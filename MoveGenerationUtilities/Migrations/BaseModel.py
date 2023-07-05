from sqlite3 import Cursor


class BaseModelClass:
    def __init__(self, table_name: str, create_query: str, con_cursor: Cursor):
        self.table_name = table_name
        self.create_table_query = create_query
        self.con_cursor = con_cursor

    def create_table(self):
        self.con_cursor.executescript(self.create_table_query)

    def drop_table(self):
        query = f'DROP TABLE IF EXISTS {self.table_name};'
        self.con_cursor.executescript(query)

    def init_table(self):
        pass

    def clear_table(self):
        query = f'DELETE FROM {self.table_name}'
        self.con_cursor.executescript(query)

    def __create_select_query(self, select_col: str = '*', where_clause: str = '') -> str:
        if len(where_clause) > 0 and 'WHERE' not in where_clause.upper():
            where_clause = 'WHERE' + where_clause
        query = f'SELECT {select_col} FROM {self.table_name} {where_clause}'
        return query

    def run_select_all(self, select_col: str = '*', where_clause: str = '') -> list:
        query = self.__create_select_query(select_col=select_col, where_clause=where_clause)
        self.con_cursor.execute(query)
        return self.con_cursor.fetchall()

    def run_select_one(self, select_col: str = '*', where_clause: str = ''):
        query = self.__create_select_query(select_col=select_col, where_clause=where_clause)
        self.con_cursor.execute(query)
        val = self.con_cursor.fetchone()
        if val is None:
            print(query)
        return val

    def print_select(self):
        print(self.run_select_all())

    def run_migration(self):
        print(f'Running migration on {self.table_name}.')
        self.drop_table()
        self.create_table()
        self.init_table()
        print(f'Migration completed on {self.table_name}.')

    @staticmethod
    def drop_all_tables(con_cursor: Cursor):
        con_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = con_cursor.fetchall()
        for table in tables:
            table_name = table[0]
            con_cursor.execute(f"DELETE FROM {table_name}")
