from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: # edge case, endword has to be in the list
            return 0
        
        queue = deque([(beginWord, 1)]) # deque with (word, step)
        visited = set([beginWord])      # start with beginWord so we don't go back to it

        while queue:
            word, steps = queue.popleft() # assign current element to word and steps
            
            for neighbor in wordList:     # check each word in wordList
                diff = 0
                for c1, c2 in zip(word, neighbor): # zip breaks each string into chars to compare
                    if c1 != c2:
                        diff += 1
                
                if diff == 1 and neighbor not in visited:
                    if neighbor == endWord:
                        return steps + 1  # steps already tracked, just add 1
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        
        return 0  # queue exhausted, no path found


# BFS Pattern — use whenever you need shortest path
#
# The core template is always the same:
#   queue = deque([start])
#   visited = set([start])
#   while queue:
#       node = queue.popleft()
#       for neighbor in neighbors:
#           if neighbor not in visited:
#               visited.add(neighbor)
#               queue.append(neighbor)
#
# If you need to track distance, store it alongside the node:
#   queue = deque([(start, 0)])
#   and pass steps + 1 when appending neighbors
#
# Key things to always remember:
#   - Use popleft() not pop() — pop() gives you DFS behavior (stack)
#   - Always mark visited WHEN you add to queue, not when you pop
#     otherwise you add the same node multiple times before processing it
#   - Return 0 at the end if queue empties without finding the target


# Patterns to study next:
#
# 1. BFS on a matrix/grid
#    Same pattern but neighbors are up/down/left/right cells.
#    Common problems: number of islands, rotting oranges, shortest path in grid.
#
# 2. DFS — the recursive cousin of BFS
#    Uses a stack instead of a queue (or just recursion).
#    Good for exploring ALL paths, not just shortest.
#    Common problems: number of islands, path sum in tree.
#
# 3. Bidirectional BFS
#    Run BFS from both start and end simultaneously.
#    They meet in the middle — much faster for large graphs.
#    Word Ladder has an optimized version using this.
#
# 4. Topological Sort
#    BFS variant for directed graphs with dependencies.
#    Common problems: course schedule, build order.
#
# 5. Dijkstra's Algorithm
#    BFS but with weighted edges — uses a priority queue (heap)
#    instead of a regular queue. Use when steps have different costs.
