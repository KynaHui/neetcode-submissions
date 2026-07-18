# [1, 2, 3, 4, 5]
# left: [1, 1, 2, 6, 4]
# right: [120, 60, 40, 5, 1]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        # <----
        for i in range(len(nums)-1, 0, -1):
            output.append(output[-1] * nums[i])
            # [1, 5, 40, 60, 120]
        output = output[::-1]

        left = 1
        # --->
        for i in range(len(nums)):
            output[i] *= left 
            left *= nums[i] # strictly increasing

        return output