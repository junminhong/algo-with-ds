# 時間複雜度 O(1)，但如果遇到 python 底層 list 擴容時，單次操作 push 或 pop 會是 O(n)
# 空間複雜度 O(n)，n 取決 stack 內容物的長度

# min stack 的概念就是在 stack push item 時，多一個 mins 的暫存檔紀錄最小值
class MinStack:
    def __init__(self):
        self._data = []
        self._mins = []

    def push(self, item):
        self._data.append(item)
        if not self._mins or item <= self._mins[-1]:
            self._mins.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        return self._data[-1] if self._data else None

    def is_empty(self):
        return not self._data

    def get_min(self):
        return self._mins[-1] if self._mins else None


min_stack = MinStack()

for x in [3, 5, 2, 1, 1, 4]:
    min_stack.push(x)
    print(f"Pushed {x}, current min = {min_stack.get_min()}")

while not min_stack.is_empty():
    top = min_stack.pop()
    print(f"Popped {top}, new min = {min_stack.get_min()}")
