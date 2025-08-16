"""
firstList = [[0,2],[5,10],[13,23],[24,25]], 
secondList = [[1,5],[8,12],[15,24],[25,26]]

[max, min]
[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
"""

def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
    firstL, secondL = len(firstList), len(secondList)
    i, j = 0, 0
    result = []

    while(i < firstL and j < secondL):
        
        left = max(firstList[i][0], secondList[j][0])
        right = min(firstList[i][1], secondList[j][1])

        if(left <= right):
            result.append([left, right])

        if(firstList[i][1] < secondList[j][1]):
            i += 1
        else:
            j += 1

    return result


            