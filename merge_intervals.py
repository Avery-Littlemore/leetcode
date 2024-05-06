# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Constraints:
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

"""
P:
Input: 
- array of 2-element subarrays
    - each subarray consists of a start and a stop point for a line segment
Output:
- array of 2-element subarrays
    - each subarray consists of a start and a stop point for a totalized/continuous line segment

- Take a group of segments as input
- if any segment overlaps another,
    - take the lower of the two mins
    - take the higher of the two maxes
    - use that as your totalized representation of the segment
- if not
    - add it 

E:
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

D:
- arrays

A:
- create a results array
- modified = False
- iterate through each subarray (interval) in intervals
    - if not results
        - append interval
    - else iterate through each results array
        - if range from result[0] to result[1] includes interval[0] or interval[1]
            - replace the current result subarray with min and max of the comparators
            - modified = True
            - break
    - if none were added or changed (modified == False)
        - insert interval
    - else
        - modified = False

- return results array with duplicates removed

"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        results = []
        intervals = sorted(intervals)
        for i in range(len(intervals)):
            if not results:
                results.append(intervals[i])
            else:
                previous_end = results[-1][1]
                current_start = intervals[i][0]
                current_end = intervals[i][1]
                if current_start <= previous_end:
                    results[-1][1] = max(current_end, previous_end)
                else:
                    results.append(intervals[i])

        return results
        