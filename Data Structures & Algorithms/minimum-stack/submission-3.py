class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float("inf")

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(val - self.minimum)
        else:
            self.stack.append(0)
            self.minimum = val

        if val < self.minimum:
            self.minimum = val

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.minimum = self.minimum - pop

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.minimum
        else:
            return self.minimum + self.stack[-1]

    def getMin(self) -> int:
        return self.minimum

