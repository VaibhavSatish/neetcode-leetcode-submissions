class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

    def pop(self) -> None:
        self.stk.pop(-1)

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return min(self.stk)
