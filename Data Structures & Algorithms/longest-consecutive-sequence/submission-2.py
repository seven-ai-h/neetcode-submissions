# start: 2 -> 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        start = 0 
        for i in set(nums):
            if i-1 not in set(nums):
                start = i
                curr = 1
                while start + 1 in set(nums):
                    curr += 1
                    start = start + 1
                longest = max(longest, curr)
        return longest
        