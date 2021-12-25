from src.dao.dao_interface import DAOInterface
from src.models.auction import Auction


class AuctionDAO(DAOInterface):
    def register(self, auction: Auction) -> None:
        command = ("INSERT INTO auctions (AUCTION_ID, NAME, INITIAL_VALUE, OPENING_DATE, "
                   "SELLER_ID, BIDS_IDS) VALUES (%s, %s, %s, %s, %s, %s)")
        self.manager.execute_sql_command(command, auction.to_tuple())
        self.manager.commit_command()

    def search_by_id(self, auction_id: int) -> Auction:
        query = "SELECT * FROM auctions a WHERE a.auction_id = %s"
        self.manager.execute_sql_command(query, (auction_id,))
        auction = self.manager.cursor.fetchone()
        return Auction(*auction)
