def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
    """
    n=4
    colors = [0,0,0,0]

    """
    count = 0
    colors = [0] * n
    result = [0] * len(queries)

    for index, (i, color) in enumerate(queries):

        # left element check with previous color if exists 
        # to make sure we don't break existing adjacent pairs
        if(i > 0 and colors[i] and colors[i - 1] == colors[i]):
            count -= 1

        # right check
        if(i < n-1 and colors[i] and colors[i + 1] == colors[i]):
            count -= 1

        # left element check
        if(i > 0 and colors[i - 1]==color):
            count += 1
        if(i < n-1 and colors[i + 1]==color):
            count += 1

        
        colors[i] = color # place color
        result[index] = count # current adjacent counts

    return result