def generateParenthesis(self, n: int) -> List[str]:
    # 3
    # ((()))
    openN, closeN = 0,0
    result = []
    stack = []

    def backtrack(openN, closeN):
        
        if(openN == closeN == n):
            result.append("".join(stack))
        
        if(openN < n):
            stack.append("(")
            backtrack(openN+1, closeN)
            stack.pop()
        
        if(openN > closeN):
            stack.append(")")
            backtrack(openN, closeN+1)
            stack.pop()

    backtrack(0,0)
    return result