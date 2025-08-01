def isValid(self, s: str) -> bool:
        
    _parenMap = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    # ([{}])
    # h
    stack = []
    for ch in s:
        if(ch in _parenMap):
            if(stack and stack[-1] == _parenMap[ch]):
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    return len(stack)==0