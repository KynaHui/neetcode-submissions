class Solution:
    # time: O(2n), space: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = [1] * n

        prefix = 1
        for i in range(n):
            results[i] = prefix
            prefix *= nums[i]
        
        postfix = 1 # store accumulated values 
        # not stop at "0"
        for i in range(n - 1, -1, -1):
            results[i] *= postfix
            postfix *= nums[i]
        return results