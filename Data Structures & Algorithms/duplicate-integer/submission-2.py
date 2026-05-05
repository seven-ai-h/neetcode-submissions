class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False

#use set for runtime purposes
#set.add is O(1) while arr.append is O(n)
#Not in: set() -> O(1), arr() -> O(n^2)
