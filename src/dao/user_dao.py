from src.models.user import User
from src.dao.dao_interface import DAOInterface


class UserDAO(DAOInterface):
    def search_by_username(self, username: str) -> User:
        query = "SELECT * FROM users u WHERE u.name = %s"
        self.manager.execute_sql_command(query, (username,))
        fetched_user = self.manager.cursor.fetchone()
        return User(*fetched_user) if fetched_user else None

    def delete_user(self, user: User) -> None:
        query = "DELETE FROM users u WHERE u.user_id = %s"
        self.manager.execute_sql_command(query, (user.user_id,))
