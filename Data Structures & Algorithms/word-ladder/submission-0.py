from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: #edge case, endword has to be in the list
            return 0
        queue = deque([(beginWord, 1)]) #deque with (word, step) 
        visited = set([beginWord]) #start with begin word

        while queue: 
            word, steps = queue.popleft() #assign current queue "cat" to word and 1 to steps
            for neighbor in wordList: #check each word in wordList
                diff = 0
                for c1, c2 in zip(word, neighbor): #zip breaks down each string into char so word and neighbor
                    if c1 != c2:
                        diff += 1
                if diff == 1 and neighbor not in visited: 
                    if neighbor == endWord:
                        return steps + 1
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        
        return 0





