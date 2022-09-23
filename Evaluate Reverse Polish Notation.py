class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        i = 0
        operators = ["+", "-", "/", "*"]
        for i in range(len(tokens)):
            if tokens[0] not in operators:
                stack.append(tokens.pop(0))
            elif tokens[0] == "+":
                tokens.pop(0)
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif tokens[0] == "/":
                first = int(stack.pop())
                second = int(stack.pop())
                tokens.pop(0)
                stack.append( int(second/first))
            elif tokens[0] == "-":
                first = int(stack.pop())
                second = int(stack.pop())
                tokens.pop(0)
                stack.append(second - first)
            elif tokens[0] == "*":
                tokens.pop(0)
                stack.append(int(stack.pop()) * int(stack.pop()))
        return int(stack[0])
