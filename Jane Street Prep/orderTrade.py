import heapq
def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
    """
    0 - buy
    1 - sell
    [price, amount, type]
    buy order - look for smallest sell order
                - if sell order <= current buy 
                - execute and remove that sell order from backlog
                - add buy order to backlog

    sell order - look for largest price in buy order
                - if buy order >= current sell
                - execute and remove buy order from backlog
                - add sell order to backlog
    buy order - maxheap
    sell order - minheap

    time : O(m * log n) n is backlog size
    space: O(n)
    """
    buy_order = []
    sell_order = []
    for price, amount, order_type in orders:
        if(order_type == 0):
            # buy
            while(amount > 0 and sell_order and sell_order[0][0] <= price):
                # execute or not
                sell_price, sell_amount = heapq.heappop(sell_order)
                if(amount >= sell_amount):
                    # trade
                    amount -= sell_amount
                else:
                    # add 
                    heapq.heappush(sell_order, (sell_price, sell_amount - amount))
                    amount = 0

            if(amount > 0):
                heapq.heappush(buy_order, (- price, amount))

        else:
            # sell
            while(amount > 0 and buy_order and -buy_order[0][0] >= price):
                buy_price, buy_amount= heapq.heappop(buy_order)

                if(amount >= buy_amount):
                    amount -= buy_amount
                else:
                    heapq.heappush(buy_order, (buy_price, buy_amount - amount))
                    amount = 0

            if(amount > 0):
                heapq.heappush(sell_order, (price, amount))

    MOD = 10**9 + 7
    total_amount = 0
    for order in buy_order + sell_order:
        total_amount += order[1]
    return total_amount % MOD

