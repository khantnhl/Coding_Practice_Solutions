def alienOrder(self, words: List[str]) -> str:
        
    adjlist = { c : set() for word in words for c in word }

    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]

        minlen = min(len(w1), len(w2))

        if(len(w1) > len(w2) and w1[:minlen] == w2[:minlen]):
            return ""

        for j in range(minlen):
            if(w1[j] != w2[j]):
                adjlist[w1[j]].add(w2[j])
                break

    print(adjlist)
    visited = {}
    result = []

    def dfs(c):
        if(c in visited):
            return visited[c]

        # backtrack path
        visited[c] = True
        for neighbor in adjlist[c]:
            if(dfs(neighbor)):
                return True
        
        visited[c] = False
        
        result.append(c)

    for ch in adjlist:
        if(dfs(ch)):
            return ""

    result.reverse()
    return "".join(result)