# time: O(n logn) + O(n^2)
# space: O(n), due to sort
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        # nums: unsorted, has duplicate
        nums.sort()
        for i, item in enumerate(nums):
            # item must be min, after sort
            if item > 0: # impossible to do
                break
            # same value as neighbor in sorted array
            if i != 0 and item == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r: 
                three_sum = item + nums[l] + nums[r]
                if three_sum > 0: # nums[l] + nums[r] > -nums[i]:
                    r -= 1
                elif three_sum < 0: # nums[l] + nums[r] < -nums[i]:
                    l += 1
                elif three_sum == 0: 
                    results.append([item, nums[l], nums[r]])
                    l += 1
                    # keep shift l until no duplicates
                    while nums[l] == nums[l-1] and l < r: 
                        l += 1

        return results