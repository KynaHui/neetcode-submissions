class Solution:
    # nums: var; List[int]: sturcture of "nums"
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            # not range(n)
            # Imagine your list is [A, B, C, D].
            # When i=0 and j=1, you check if A == B.
            # Later, when i=1 and j=0, you would check if B == A
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
