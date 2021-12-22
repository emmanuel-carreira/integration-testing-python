from src.models.user import User
from src.postgres import Postgres


class UserDAO:
    def __init__(self, manager: Postgres):
        self.manager = manager

    def search_by_username(self, username: str):
        query = "SELECT u FROM users u WHERE u.name = %s"
        self.manager.execute_sql_command(query, (username,))
        return self.manager.cursor.fetchone()

    def delete_user(self, user: User):
        pass
