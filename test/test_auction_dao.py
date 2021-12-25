from datetime import datetime
import os
import unittest

from src.dao.auction_dao import AuctionDAO
from src.models.auction import Auction
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
            CREATE TABLE IF NOT EXISTS auctions
            (AUCTION_ID    INT          PRIMARY KEY NOT NULL,
             NAME          VARCHAR(100)             NOT NULL,
             INITIAL_VALUE REAL,
             OPENING_DATE  TIMESTAMP,
             SELLER_ID     INT,
             BIDS_IDS      INT[]);""")
        cls.postgres.commit_command()

        cls.auction_dao = AuctionDAO(cls.postgres)

    def setUp(self):
        self.postgres.execute_sql_command("DELETE FROM auctions;")
        self.postgres.commit_command()

    def test_auction_registration(self):
        auction = Auction(1, "Knapsack", 10.0, datetime.utcnow(), 1, [])

        self.auction_dao.register(auction)

        registered_auction = self.auction_dao.search_by_id(auction.auction_id)
        self.assertIsNotNone(registered_auction)
