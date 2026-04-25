class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if sorted, duplicates are next to each other
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False