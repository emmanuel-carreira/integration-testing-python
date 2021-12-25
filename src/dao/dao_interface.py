# pylint: disable=too-few-public-methods

from src.postgres import Postgres


class DAOInterface:
    def __init__(self, manager: Postgres):
        self.manager = manager
