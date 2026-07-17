class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # pair = [index, temp]

        for index, temp in enumerate(temperatures):
            # stack[-1]: top of stack, pair[1]: temp
            while stack and temp > stack[-1][1]:
                sIndex, sTemp = stack.pop()
                result[sIndex] = index - sIndex
            stack.append([index, temp])
        return result