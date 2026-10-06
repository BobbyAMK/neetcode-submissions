class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpd = list(zip(position, speed))
        stack = []

        for pos, spd in sorted(posAndSpd):
            time = (target - pos) / spd
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)