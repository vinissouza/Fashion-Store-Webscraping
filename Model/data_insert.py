import pandas
import pandas as pd
import sqlite3
from sqlalchemy import create_engine


class DataInsert:
    def __init__(self, data: pd.DataFrame, table_name: str, sql_database='hm_db.sqlite'):
        self.data = data
        self.table_name = table_name
        self.sql_database = sql_database

        # create connection object
        #conn = sqlite3.connect(self.sql_database)

        self.db = create_engine(f'sqlite:///{self.sql_database}', echo=False)
        self.conn = self.db.connect()

        # # connect to database
        # self.conn = create_engine(f'sqlite:///{self.sql_database}', echo=False)

    def check_table_exist(self):
        tables_query = """
            SELECT name 
            FROM sqlite_master 
            WHERE type = 'table'
        """

        database_tables = pd.read_sql_query(tables_query, self.conn)

        result = self.table_name in database_tables['name'].values

        return result

    def columns_query(self, data):
        columns_type = pd.DataFrame(data.dtypes).reset_index()

        columns_type.columns = ['columns', 'types']

        sql_types = {'None': 'NULL',
                     'int64': 'INTEGER',
                     'float64': 'REAL',
                     'object': 'TEXT'}

        columns_type['types'] = columns_type['types'].astype(str).map(sql_types)

        query_schema = str()

        for i in range(len(columns_type)):
            query_schema += f"{columns_type['columns'][i]} {columns_type['types'][i]}, "

        columns_schema = query_schema[:-2]

        return columns_schema

    def check_columns(self):
        columns_query = f"""
            SELECT * FROM  {self.table_name}
        """

        table = pd.read_sql_query(columns_query, self.conn)

        new_columns = set(self.data.columns).symmetric_difference(set(table.columns))

        if len(new_columns) != 0:
            data_columns = self.data[list(new_columns)]

            columns_schema = self.columns_query(data_columns)

            # columns_types = pd.DataFrame(data_columns).reset_index()
            #
            # columns_types.columns = ['columns', 'types']
            #
            # sql_types = {'None': 'NULL', 'int64': 'INTEGER', 'float64': 'REAL', 'object': 'TEXT'}
            #
            # columns_types['types'] = columns_types['types'].astype(str).map(sql_types)
            #
            # query_new_columns = str()
            #
            # for i in range(len(columns_types)):
            #     query_new_columns += f"{columns_types['columns'][i]} {columns_types['types'[i]]}, "
            #
            # columns_schema = query_new_columns[:-2]

            add_columns_query = f"""
                ALTER TABLE {self.table_name}
                ADD {columns_schema}
            """

            self.conn.execute(add_columns_query)

            #self.conn.commit()

        return None

    def insert_data(self):

        table_exists = self.check_table_exist()

        if table_exists:
            self.check_columns()

            self.data.to_sql(self.table_name, con=self.conn, if_exists='append', index=False)

        else:
            columns_schema = self.columns_query(self.data)

            # columns_types = pd.DataFrame(self.data.dtypes).reset_index()
            #
            # columns_types.columns = ['columns', 'types']
            #
            # sql_types = {'None': 'NULL', 'int64': 'INTEGER', 'float64': 'REAL', 'object': 'TEXT'}
            #
            # columns_types['types'] = columns_types['types'].astype(str).map(sql_types)
            #
            # query_schema = str()
            #
            # for i in range(len(columns_types)):
            #     query_schema += f"{columns_types['columns'][i]} {columns_types['types'][i]}, "
            #
            # columns_schema = query_schema[:-2]

            query_schema = f"""CREATE TABLE {self.table_name} ( {columns_schema} )"""

            self.conn.execute(query_schema)

            #self.conn.commit()

            self.data.to_sql(
                self.table_name, con=self.conn, if_exists='append', index=False
            )

        return print(f"Data has been insert in {self.table_name} ")

    def __enter__(self):
        # connect to database
        # self.conn = create_engine(f'sqlite:///{self.sql_database}', echo=False)

        self.db = create_engine(f'sqlite:///../Datasets/{self.sql_database}', echo=False)
        self.conn = self.db.connect()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        self.db.dispose()

        print(f'Connection with {self.sql_database} closed!')




