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
        prereq_hash = {}
        for i in range(numCourses):
            prereq_hash[i] = []

        for course, pre in prerequisites:
            prereq_hash.setdefault(course, []).append(pre)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            
            if prereq_hash[course] == []:
                return True
            
            visited.add(course)

            for val in prereq_hash.get(course, []):
                if not dfs(val):
                    return False
            
            visited.remove(course)
            prereq_hash[course] = []
            return True

        for course in prereq_hash:
            if not dfs(course): 
                return False

        return True
