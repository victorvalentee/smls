"""Generic Data Client.

Props to Todd Birchard for writing this `beautiful piece of code`_.

.. _beautiful piece of code:
    https://hackersandslackers.com/bigquery-and-sql-databases/
"""

from sqlalchemy import MetaData, Table


class DataClient:
    def __init__(self, engine):
        self.engine = engine
        self.metadata = MetaData(bind=self.engine)
        self.table_name = None

    @property
    def table(self):
        if self.table_name:
            return Table(self.table_name, self.metadata, autoload=True)
        return None

    def fetch_rows(self, query, table=None):
        """Fetch all rows from `query` result."""
        rows = self.engine.execute(query).fetchall()
        return rows

    def insert_rows(self, rows, table=None, replace=None):
        """Insert rows into table."""
        if replace:
            self.engine.execute(f'TRUNCATE TABLE {table}')
        self.table_name = table
        self.engine.execute(self.table.insert(), rows)
        return self.construct_response(rows, table)

    @staticmethod
    def construct_response(rows, table):
        """Summarize results of an `insert_rows()` call."""
        columns = rows[0].keys()
        column_names = ", ".join(columns)
        num_rows = len(rows)
        return f'Inserted {num_rows} rows into `{table}` with {len(columns)} columns: {column_names}'
