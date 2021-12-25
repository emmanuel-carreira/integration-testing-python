import os
import unittest

from src.dao.user_dao import UserDAO
from src.models.user import User
from src.postgres import Postgres

class UserDAOTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.postgres = Postgres(
            host=os.environ.get("POSTGRES_HOST"),
            port=os.environ.get("POSTGRES_PORT"),
            database=os.environ.get("POSTGRES_DATABASE"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD")
        )

        cls.postgres.execute_sql_command("""
            CREATE TABLE IF NOT EXISTS users
            (USER_ID  INT          PRIMARY KEY NOT NULL,
             NAME     VARCHAR(100)             NOT NULL,
             EMAIL    VARCHAR(100),
             PASSWORD VARCHAR(64),
             ROLE     VARCHAR(20),
             ENABLED  BOOL);""")
        cls.postgres.commit_command()

        cls.user_dao = UserDAO(cls.postgres)

    def setUp(self):
        self.postgres.execute_sql_command("DELETE FROM users;")
        self.postgres.commit_command()

    def test_search_by_username_when_user_with_given_username_does_not_exist(self):
        user = self.user_dao.search_by_username("John")

        self.assertEqual(user, None)

    def test_search_by_username_when_user_with_given_username_exists(self):
        self.postgres.execute_sql_command(
            "INSERT INTO users (USER_ID, NAME) VALUES (%s, %s)",
            (1, "Jack")
        )
        self.postgres.commit_command()

        user = self.user_dao.search_by_username("Jack")

        self.assertIsInstance(user, User)
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.name, "Jack")
