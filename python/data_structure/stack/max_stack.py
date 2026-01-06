class MaxStack:
    def __init__(self):
        self._data = []
        self._maxs = []

    def push(self, item):
        self._data.append(item)
        # 可以仔細發現 max stack 和 min stack 差異僅在這裡
        if not self._maxs or item >= self._maxs[-1]:
            self._maxs.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        return self._data[-1] if self._data else None

    def is_empty(self):
        return not self._data

    def get_max(self):
        return self._maxs[-1] if self._maxs else None

max_stack = MaxStack()

for x in [3, 5, 2, 1, 1, 4]:
    max_stack.push(x)
    print(f"Pushed {x}, current max = {max_stack.get_max()}")

while not max_stack.is_empty():
    top = max_stack.pop()
    print(f"Popped {top}, new max = {max_stack.get_max()}")
