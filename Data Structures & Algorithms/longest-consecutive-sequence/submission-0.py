# time: O(n), memory: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # search in set: O(1), list: O(n)
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            # left check: if it is the start of a sequence
            if n - 1 not in nums_set:
                # number tracker + sequence counter
                length = 0 

                # right check
                while n + length in nums_set:
                    length += 1
                # longest = max(length, longest)
                if length > longest:
                    longest = length
        return longest