class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        return self._data[-1] if self._data else None

    def is_empty(self):
        return not self._data

stack = Stack()
for x in [3, 5, 2, 1, 1, 4]:
    stack.push(x)
    print(f"Pushed {x}")

# 由此可觀察出 Stack 特性是先進後出
while not stack.is_empty():
    top = stack.pop()
    print(f"Popped {top}")
