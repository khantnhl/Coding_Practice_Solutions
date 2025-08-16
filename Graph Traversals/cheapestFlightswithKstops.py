"""
"""
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    
    """shortest path finder algorithm"""
    # build adjlist
    from collections import deque, defaultdict
    adjlist = defaultdict(list)

    for sc, dest, cost in flights:
        adjlist[sc].append([dest, cost])
    # 0->[1, 100]
    # prices = [inf,inf..]

    prices = [float('inf')] * n
    prices[src] = 0

    queue = deque([(0, src, 0)]) # queue = [cost, city, total_stop]

    while(queue):
        curPrice, currStop, stops = queue.popleft()

        if(stops > k):
            continue

        for neighbor, weight in adjlist[currStop]:
            nextCost = curPrice + weight

            if(nextCost < prices[neighbor]):
                prices[neighbor] = nextCost
                queue.append((nextCost, neighbor, stops + 1))

    return prices[dest] if(prices[dest]!= float('inf')) else -1

