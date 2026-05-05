class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # {number_value: its_index}
        for i, n in enumerate(nums): # index-element pair
            diff = target - n
            if diff in prevMap:
                # prevMap[diff] -> return index 
                return [prevMap[diff], i]
            # cant find in hashMap, add n:i to prevMap
            prevMap[n] = i
        return       