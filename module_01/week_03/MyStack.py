
class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.stack = []

    def get_capacity(self):
        return self.__capacity

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.__capacity

    def pop(self):
        return self.stack.pop(-1)

    def push(self, value):
        return self.stack.append(value)

    def top(self):
        return self.stack[-1]


if __name__ == "__main__":
    stack1 = MyStack(5)
    stack1.push(1)
    stack1.push(2)
    print(stack1.is_full())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.is_empty())
