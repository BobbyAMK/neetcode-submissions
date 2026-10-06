class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                if len(stack) > 1:
                    b, a = stack.pop() , stack.pop()
                    stack.append(operators[i](a, b))
        return stack[0]
