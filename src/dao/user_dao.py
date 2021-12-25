from src.models.user import User
from src.postgres import Postgres


class UserDAO:
    def __init__(self, manager: Postgres):
        self.manager = manager

    def search_by_username(self, username: str) -> User:
        query = "SELECT * FROM users u WHERE u.name = %s"
        self.manager.execute_sql_command(query, (username,))
        fetched_user = self.manager.cursor.fetchone()
        return User(*fetched_user) if fetched_user else None

    def delete_user(self, user: User):
        pass
