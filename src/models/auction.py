from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Auction:
    auction_id: int
    name: str
    initial_value: float
    opening_date: datetime
    seller_id: int
    bids_ids: List[int]

    def to_tuple(self):
        return (self.auction_id, self.name, self.initial_value,
                self.opening_date, self.seller_id, self.bids_ids)
