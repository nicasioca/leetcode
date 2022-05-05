class MyStack:

    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    def push(self, x: int) -> None:
        self.q1.appendleft(x)

    def pop(self) -> int:
        while len(self.q2) > 0:
            self.q1.appendleft(self.q2.pop())
        while len(self.q1) > 1:
            self.q2.appendleft(self.q1.pop())
        return self.q1.pop()

    def top(self) -> int:
        while len(self.q2) > 0:
            self.q1.appendleft(self.q2.pop())
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False