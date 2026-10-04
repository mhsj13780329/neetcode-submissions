class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []
        operations = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operations:
                op_stack.append(int(token))
            else:
                match token:
                    case "+":
                        res = op_stack[-2] + op_stack[-1]
                    case "-":
                        res = op_stack[-2] - op_stack[-1]
                    case "/":
                        res = int(op_stack[-2] / op_stack[-1])
                    case "*":
                        res = op_stack[-2] * op_stack[-1]
                op_stack.pop()
                op_stack.pop()
                op_stack.append(res)

        return op_stack[0]

