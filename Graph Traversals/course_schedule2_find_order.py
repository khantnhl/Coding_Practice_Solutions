"""
time : O(v + e)
space: O(v + e)
"""
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
    from collections import defaultdict, deque

    adjlist = defaultdict(list)
    indeg = [0] * numCourses

    for course, prereq in prerequisites:
        adjlist[prereq].append(course)
        indeg[course] += 1

    queue = deque([v for v in range(numCourses) if(indeg[v]==0)])

    result = []
    while(queue):
        curr = queue.popleft()
        result.append(curr)

        for neighbor in adjlist[curr]:
            indeg[neighbor] -= 1

            if(indeg[neighbor]==0):
                queue.append(neighbor)

    if(len(result)==numCourses):
        return result
    else:
        return []
