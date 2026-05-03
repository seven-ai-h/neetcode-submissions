# prerequisites[i] = [a, b] -> each element is a list that contains a and b
# you have to take b prior to take course a -> [0, 1] take course 1 before to take course 0
# numCourses -> # of courses required to take, length is 0 to numCourses - 1(array similar)
# return an ordering of courses -> return a list in the right order
# if impossible -> return empty array
# numCourses 4. so length will be [0,1,2,3]. prereq = [0,2] -> [2, 0, 1, 3]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency dictionary — key is course, value is list of its prerequisites
        # always convert edge list input into adjacency structure before doing DFS/BFS
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)

        # three state tracking — you decide what 0, 1, 2 mean, DFS doesn't know automatically
        # 0 = unvisited, 1 = visiting (currently in DFS path), 2 = visited (fully processed)
        # use [0] * numCourses not just [0] — list needs a slot for every course
        state = [0] * numCourses
        result = []

        # DFS is defined inside findOrder so it can access adj, state, result directly
        def dfs(course):
            if state[course] == 2:  # already fully processed, safe to skip
                return True
            if state[course] == 1:  # currently being visited — cycle detected!
                return False

            state[course] = 1  # mark as visiting before going deeper

            for prereq in adj[course]:
                if not dfs(prereq):  # if any prerequisite has a cycle, bubble False up
                    return False

            # only add to result AFTER all prerequisites are processed
            # this guarantees prerequisites always appear before the course
            state[course] = 2
            result.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):  # if cycle detected anywhere, return empty
                return []

        return result


# What you used and why:
#
# Adjacency dictionary — converted the edge list [a, b] into {course: [prereqs]}
#   so DFS can instantly look up prerequisites for any course in O(1)
#
# DFS — goes deep into prerequisites first, adds them to result, then adds current course
#   this naturally produces the correct topological order
#
# Three state array — tracks visited/visiting/unvisited for every course
#   the visiting state is what detects cycles — if you land on a visiting node
#   you've looped back to something already in progress


# Concepts you missed during coding:
#
# 1. state = [0] * numCourses not just [0]
#    always multiply by the size you need, otherwise list index goes out of bounds
#
# 2. append() uses parentheses not brackets
#    adj[a].append(b) not adj[a].append[b]
#
# 3. calling a function uses parentheses
#    dfs(i) not dfs[i]
#
# 4. checking state needs the index
#    state[course] == 1 not state == 1
#
# 5. after the DFS loop, handle the cycle case
#    if not dfs(i): return [] — without this, cycles are silently ignored
#
# 6. nest DFS inside the outer function
#    so it can access adj, state, result without passing them as arguments


# Patterns to study next:
#
# 1. Topological sort with BFS (Kahn's algorithm)
#    instead of DFS, use indegree counting + queue
#    indegree = number of prerequisites a course has
#    start with courses that have 0 prerequisites, work outward
#
# 2. Graph cycle detection
#    the three state pattern (unvisited/visiting/visited) is the standard way
#    to detect cycles in directed graphs — memorize it
#
# 3. Number of connected components
#    run DFS/BFS from every unvisited node, count how many times you start fresh
#    uses the same visited tracking pattern
#
# 4. Dijkstra's algorithm
#    weighted graph shortest path — BFS with a min heap instead of a queue
#    builds on the adjacency dictionary pattern used here
