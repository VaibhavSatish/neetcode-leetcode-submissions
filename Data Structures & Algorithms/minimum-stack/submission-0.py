class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.insert(0, val)

    def pop(self) -> None:
        self.stk.pop(0)

    def top(self) -> int:
        return self.stk[0]

    def getMin(self) -> int:
        return min(self.stk)
