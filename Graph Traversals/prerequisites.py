# Given a list of courses that a student needs to take to complete their major 
# and a map of courses to their prerequisites, 
# return a valid order for them to take their courses assuming they only take one course for their major at once.

# Examples:
# Input: ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], 
# { "Data Structures": ["Intro to Programming"], 
# "Advanced Algorithms": ["Data Structures"], 
# "Operating Systems": ["Advanced Algorithms"], 
# "Databases": ["Advanced Algorithms"] 
# }

# Output: ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"] or 
# ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Databases", "Operating Systems"]

# Topological Sorting 
from collections import deque
def prerequisite(courselist, adjlist):

    indeg = { v: 0 for v in courselist}

    # iterate over each course
    for course in adjlist:
        # course each prereq
        for prereq in adjlist[course]:
            indeg[prereq] += 1

    queue = deque([v for v in courselist if indeg[v] == 0]) 
    result = []

    while(queue):

        curr = queue.popleft()
        result.append(curr)
        
        for neighbor in adjlist.get(curr, []):
            indeg[neighbor] -= 1

            if(indeg[neighbor] == 0):
                queue.append(neighbor)

    return result[::-1] if result else -1

print(prerequisite(["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], 
             { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }))
