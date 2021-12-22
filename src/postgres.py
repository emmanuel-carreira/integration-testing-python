# pylint: disable=too-many-arguments

import psycopg2


class Postgres:
    def __init__(self, host: str, port: str, database: str, user: str, password: str):
        self._connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        self._cursor = None

    def __del__(self):
        if self._cursor:
            self._cursor.close()
        self._connection.close()

    @property
    def cursor(self):
        if not self._cursor:
            self._cursor = self._connection.cursor()
        return self._cursor

    def execute_sql_command(self, command: str, params = ()):
        self.cursor.execute(command, params)

    def commit_command(self):
        self._connection.commit()
