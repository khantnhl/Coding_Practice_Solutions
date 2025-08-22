def findCircleNum(self, isConnected: List[List[int]]) -> int:
    provinces = 0
    visited = set()

    def dfs(city):
        visited.add(city)

        # for each cell in row
        for cur, connected in enumerate(isConnected[city]):
            if(connected==1 and cur not in visited):
                dfs(cur)
    
    # for each row
    for i in range(len(isConnected)):
        if(i not in visited):
            dfs(i)
            provinces += 1
    
    return provinces