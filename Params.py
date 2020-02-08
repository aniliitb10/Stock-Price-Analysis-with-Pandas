from enum import IntEnum


class Params (IntEnum):
    OpenInterest = 1,
    ChangeInOpenInterest = 2,
    LastTradedPrice = 3,
    NetChange = 4,
    Volume = 5,
    BidQuantity = 6,
    BidPrice = 7,
    OfferPrice = 8,
    OfferQuantity = 9,
    StrikePrice = 10,
