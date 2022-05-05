class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        self.s1.append(x)

    def pop(self) -> int:
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        return self.s2[-1]
            
    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false