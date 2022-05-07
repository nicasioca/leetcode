import math
from collections import Counter

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      res = []
      overlap = [-1]*len(intervals)

      # return new interval if empty
      if intervals == []:
        return [newInterval]

      # verify if overlaps exist
      for idx, inter in enumerate(intervals):
        for i in range(inter[0], inter[1]+1):
          for j in range(newInterval[0], newInterval[1]+1):
            if i == j:
              overlap[idx] = idx

      # merge the existing overlap intervals
      count = Counter(overlap)
      if len(count.keys()) > 1 or -1 not in count.keys():
        start = math.inf
        end = -math.inf
        for idx, inter in enumerate(intervals):
          if overlap[idx] != -1:
            start = min(start, inter[0])
            end = max(end, inter[1])
        mergeInterval = [start, end]

        # merge the new interval with the overlapping intervals
        start = math.inf
        end = -math.inf
        for i in range(mergeInterval[0], mergeInterval[1]+1):
          for j in range(newInterval[0], newInterval[1]+1):
            start = min(start, i, j)
            end = max(end, i, j)
        mergeIntervalFinal = [start, end]

        # create final result of intervals
        change = 0
        for idx, inter in enumerate(intervals):
          if overlap[idx] == -1:
            res.append(inter)
          else:
            if change == 0:
              res.append(mergeIntervalFinal)
              change += 1

        return res
      else:
        # handle if new interval insert at beginning
        if intervals[0][0] > newInterval[0] and intervals[0][1] > newInterval[1]:
            intervals.insert(0, newInterval)
            return intervals
            
        # handle if new interval insert at end
        if intervals[-1][0] < newInterval[0] and intervals[-1][1] < newInterval[1]:
            intervals.append(newInterval)
            return intervals

        # handle the non-overlapping case of inserting new interval in between
        for i in range(1, len(intervals)):
          if intervals[i-1][0] < newInterval[0] and intervals[i-1][1] < newInterval[1] \
              and intervals[i][0] > newInterval[0] and intervals[i][1] > newInterval[1]:
            intervals.insert(i, newInterval)
            return intervals

      # return if no change
      return intervals


# 152 / 156 test cases passed.
# Time Limit Exceeded

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].