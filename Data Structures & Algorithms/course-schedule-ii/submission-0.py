# prerequisites[i] = [a, b] -> each element is a list that contains a and b
# you have to take b prior to take course a -> [0, 1] take course 1 before to take course 0
# numCourses -> # of courses required to take, length is 0 to numCourses - 1(array similar)
# return an ordering of courses -> return a list in the right order
# if impossible -> return empty array
# numCourses 4. so length will be [0,1,2,3]. prereq = [0,2] -> [2, 0, 1, 3]
class Solution: 
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)} # adj: {1:[], 2:[], 3[]...}
        state = [0] * numCourses
        result = []
        
        for a, b in prerequisites:
            adj[a].append(b) #puts prereq in the correspond course number
        
        def dfs(course):
            if state[course] == 2:
                return True
            if state[course] == 1:
                return False
            
            state[course] = 1
            
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            
            state[course] = 2
            result.append(course)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return result
            

        