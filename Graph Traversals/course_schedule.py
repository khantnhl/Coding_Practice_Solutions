"""
Kahn's algorithm (toposort)
time : O(v + e)
space: O(v + e)
"""

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # topo sort
    from collections import defaultdict
    adjlist = defaultdict(list)
    indeg = [0] * numCourses

    for course, prereq in prerequisites:
        adjlist[prereq].append(course)
        indeg[course] += 1

    from collections import deque
    queue = deque([v for v in range(numCourses) if(indeg[v]==0)])

    while(queue):
        curr = queue.popleft()
        numCourses -= 1

        for neighbor in adjlist[curr]:
            indeg[neighbor] -= 1
            
            if(indeg[neighbor]==0):
                queue.append(neighbor)

    return (numCourses==0)
