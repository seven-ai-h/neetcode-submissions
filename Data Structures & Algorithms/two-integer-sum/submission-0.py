class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #goal: {3:0, 4:1, 5:2}
        for i in range(len(nums)): #[3,4,5] target: 8 
            curr = nums[i]
            diff = target - curr
            if diff in seen:
                return [seen[diff], i]
            seen[curr] = i #add the item to seen {3:0}


                
