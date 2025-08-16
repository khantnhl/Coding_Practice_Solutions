def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
            0       1
        [[1,2,7],[3,6,7]]
        {
            1 : 0
            2 : 0
            7 : [0,1]
            3 : 1
            6 : 1
        }

        adjlist undirected graph for routes
        0:[1]
        1:[0]

        """
        if(source == target):
            return 0

        from collections import defaultdict, deque
        routeSets = [set(route) for route in routes]
        stopsToRoute = defaultdict(list)

        for i, route in enumerate(routeSets):
            for stop in route:
                stopsToRoute[stop].append(i)

        if(source not in stopsToRoute or target not in stopsToRoute):
            return -1 
            
        adjlist = defaultdict(list)
        for route_i in stopsToRoute.values():
            num_buses = len(route_i)
            for i in range(num_buses):
                for j in range(i + 1, num_buses):
                    adjlist[route_i[j]].append(route_i[i])
                    adjlist[route_i[i]].append(route_i[j])
    
        queue = deque(stopsToRoute[source])
        visited = set(stopsToRoute[source])

        taken = 1
        while(queue):
            for _ in range(len(queue)):

                currRoute = queue.popleft()

                if(target in routeSets[currRoute]):
                    return taken

                for neighbor in adjlist[currRoute]:
                    if(neighbor not in visited):
                        visited.add(neighbor)
                        queue.append(neighbor)
            taken += 1

        return -1