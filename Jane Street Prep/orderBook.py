"""
Design an orderbook system from scratch, 
what would these APIs look like?
    - addOrder
    - cancelOrder
    - updateOrder
    - getBestBid
    - getBestAsk
    - getDepth
    - matchOrder 
"""
from collections import defaultdict, deque
import bisect
class Order():
    def __init__(self, order_id: str, side: str, price: float, quantity: int, timestamp: int):
        self.order_id = order_id
        self.side = side    # "BUY" or "SELL"
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp

class OrderBook:
    def __init__(self):
        self.bids = defaultdict(list) # store price : deque()
        self.asks = defaultdict(list) # store price : deque()

        self.bid_prices = [] # sorted descend
        self.ask_prices = [] # sorted ascend

        self.orders = {} # map

    def addOrder(self, newOrder : Order):
        """insert new order into Book"""
        prices = self.bid_prices if(newOrder.side=="BUY") else self.ask_prices
        _map = self.bids if(newOrder.side=="BUY") else self.asks

        if(newOrder.order_id not in _map):
            _map[newOrder.price] = deque()

            if(newOrder.side=="BUY"):
                # negate values just to maintain descending order
                bisect.insort_left(prices, - newOrder.price)
            else:
                bisect.insort_right(prices, newOrder.price)
                
        # {100 : o1}
        _map[newOrder.price].append(newOrder)
        self.orders[newOrder.order_id] = (newOrder.side, newOrder.price, newOrder.order_id)

    def cancelOrder():
        pass

    def updateOrder():
        pass

    def getBestBid():
        pass

    def getBestAsk():
        pass

    def getDepth():
        pass

    def matchOrder():
        pass
