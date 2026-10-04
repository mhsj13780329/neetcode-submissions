class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                match token:
                    case "+":
                        stack.append(op1 + op2)
                    case "-":
                        stack.append(op1 - op2)
                    case "/":
                        stack.append(int(op1 / op2))
                    case "*":
                        stack.append(op1 * op2)
                
        return stack[0]

