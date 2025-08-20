# You are given two words, beginWord and endWord, 
# and also a list of words wordList. All of the given words are of the same length, consisting of lowercase English letters, and are all distinct.
# Your goal is to transform beginWord into endWord by rules:
    # You may transform beginWord to any word within wordList, provided that at exactly one position the words have a different character, and the rest of the positions have the same characters.
    # You may repeat the previous step with the new word that you obtain, and you may do this as many times as needed.
# Return the minimum number of words 
# within the transformation sequence needed to obtain the endWord, 
# or 0 if no such sequence exists.

"""
Input: beginWord = "cat", 
endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]
Output: 4
Explanation: The transformation sequence is "cat" -> "bat" -> "bag" -> "sag".


{
    *at : [cat,bat]
    c*t : [cat]
    ca* : [cat]
}

use BFS traversal
"""
from typing import List
def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    
    from collections import defaultdict, deque
    adjlist = defaultdict(list)
    wordList.append(beginWord)

    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            adjlist[pattern].append(word)

    visited = set([beginWord])
    queue = deque([beginWord])
    result = 1
    while(queue):
        for _ in range(len(queue)):
            curWord = queue.popleft()

            if(curWord == endWord):
                return result
            
            # generate pattern & find edge in graph to traverse
            for i in range(len(curWord)):
                pattern = curWord[:i] + "*" + curWord[i+1:]
                for neighborWord in adjlist[pattern]:
                    visited.add(neighborWord)
                    queue.append(neighborWord)
        
        result += 1    
    
    return 0