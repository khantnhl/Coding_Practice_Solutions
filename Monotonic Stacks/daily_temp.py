def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # brute force O(n^2)
    # result = [0] * len(temperatures)
    # for i in range(len(temperatures)):
    #     track=1
    #     for j in range(i+1, len(temperatures)):
    #         if(temperatures[j] > temperatures[i]):
    #             result[i] = track
    #             break    
    #         track += 1
    # return result
    """
    monotonic stack
    """
    stack = []
    result = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        while(stack and temp > stack[-1][1]):
            past_idx, val = stack.pop()
            result[past_idx] = i - past_idx
            print(past_idx)
        stack.append([i, temp])
    return result