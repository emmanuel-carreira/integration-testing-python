from dataclasses import dataclass


@dataclass
class Bid:
    bid_id: int
    value: float
    bidder_id: int
