class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        # create a stack with pairs temp,idx
        # get temp: stack[<top of stack idx>][0]
        # get idx: stack[<top of stack idx>][1]
        stack = []

        for idx, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                _, i = stack.pop()
                result[i] = idx - i
            stack.append([val, idx])
        return result