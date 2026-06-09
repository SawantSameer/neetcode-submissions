class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        del self.arr[-1]

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        temp = []
        mini = self.arr[-1]

        while len(self.arr):
            mini = min(mini,self.arr[-1])
            temp.append(self.arr.pop())

        while len(temp):
            self.arr.append(temp.pop())

        return mini