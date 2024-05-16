# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

"""
Think of it like a directional graph where no cycles are allowed... 
(Could be multilpe trees)
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prereqs_hash = {}
        def course_relationships():
            for post, pre in prerequisites:
                prereqs_hash.setdefault(pre, []).append(post)

        course_relationships()
        outer_visited = set()

        def dfs(key, inner_visited):
            if key in inner_visited:
                print(key)
                print(outer_visited)
                print(inner_visited)
                return True
            
            inner_visited.add(key)
            if key not in outer_visited:
                outer_visited.add(key)

            if key in prereqs_hash:
                for val in prereqs_hash[key]:
                    if dfs(val, inner_visited.copy()):
                        return True
                    
            return False 
        
        def cycle_found(key):
            inner_visited = set()
            return dfs(key, inner_visited)

        for key in prereqs_hash:
            if cycle_found(key):
                print('here')
                return False

        return len(outer_visited) <= numCourses
