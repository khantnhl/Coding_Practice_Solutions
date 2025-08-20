"""


Input: tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
Output: ["JFK","BUF","HOU","SEA"]

start "JFK" 

idea: 
    directed graph
    need to sort the inputs of adjlist to have the correct order 
    use Backtracking to get the valid path

time : O(E * V)
space: O(E * V)    
"""
from typing import List

def findItinerary(self, tickets: List[List[str]]) -> List[str]:

    adjlist = { v:[] for v, dest in tickets}

    tickets.sort()
    for src, dest in tickets:
        adjlist[src].append(dest)

    result = ["JFK"]

    # BackTrackking
    def dfs(src):
        # Base Cases
        if(len(result) == len(tickets) + 1):
            return True
        
        if(src not in adjlist):
            return False

        temp = list(adjlist[src])
        for i, neighbor in enumerate(temp):
            adjlist[src].pop(i)
            result.append(neighbor)
            
            if(dfs(neighbor)):
               return True
            
            adjlist[src].insert(i, neighbor)
            result.pop()

        return False

    dfs("JFK")
    return result

