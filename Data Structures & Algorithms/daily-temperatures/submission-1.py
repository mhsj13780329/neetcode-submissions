class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            
            current_temperature = temperatures[i]
            if len(stack) == 0:
                stack.append(i)
            else:
                while current_temperature > temperatures[stack[-1]]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(i)

        return result
