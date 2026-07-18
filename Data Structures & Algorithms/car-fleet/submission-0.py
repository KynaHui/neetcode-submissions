class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p, s in sorted(zip(position, speed), reverse=True):
            time_taken = (target - p) / s
            if not stack or time_taken > stack[-1]:
                stack.append(time_taken)
        return len(stack)