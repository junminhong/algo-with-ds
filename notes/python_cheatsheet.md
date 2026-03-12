# Python Cheatsheet

## 1) 基本操作：輸入/輸出

```python
# 單行字串
s = input().strip()

# 整數
n = int(input())

# 一行多數字 -> list[int]
arr = list(map(int, input().split()))

# 多行輸入（直到 EOF）
import sys
lines = [line.strip() for line in sys.stdin]

# 輸出
print("Hello", n)
```

## 2) 核心容器與常用操作

### List（動態陣列）

```python
arr = [1, 2, 3]
arr.append(4)         # [1,2,3,4]
x = arr.pop()         # 移除最後一個並回傳
arr[1:3]              # 切片 [2,3]
arr.sort()            # 就地排序（升序）
new_arr = sorted(arr) # 回傳新排序
arr.reverse()         # 原地反轉
```

### Dict（雜湊表 / HashMap）

```python
d = {"a": 1, "b": 2}
d["c"] = 3
d.get("a", 0)         # 若無 key，回傳預設 0
for k, v in d.items():
    print(k, v)
```

### Set / Frozenset（集合）

```python
s = {1, 2, 3}
s.add(4)
s.remove(2)           # 不存在會 KeyError
s.discard(5)          # 不存在也不報錯
3 in s                # O(1) 查詢
fs = frozenset([1,2,3])  # 不可變，可當 dict key
```

### Tuple（不可變序列）

```python
t = (1, 2, 3)
d = {t: "value"}      # 可當 dict key
```

## 3) 常用函式與語法糖

```python
# enumerate
for i, val in enumerate(arr):
    print(i, val)

# zip
for a, b in zip([1,2], [3,4]):
    print(a, b)

# list / set / dict comprehension
squares = [x*x for x in range(5)]
uniq = {x % 3 for x in range(10)}
index_map = {v: i for i, v in enumerate(arr)}

# 其他常用
max_val = max(arr); min_val = min(arr)
total = sum(arr); length = len(arr)
any_true = any(x > 0 for x in arr)
all_true = all(x > 0 for x in arr)
```

## 4) collections 模組（刷題必備）

```python
from collections import Counter, defaultdict, deque, namedtuple

# Counter：統計頻次
cnt = Counter("banana")
cnt["a"]        # 3
cnt.most_common(2)  # 前2高頻

# defaultdict：自動給預設值
g = defaultdict(list)
g["u"].append("v")

# deque：雙端佇列（O(1) 頭尾操作）
dq = deque([1,2,3])
dq.appendleft(0); dq.append(4)
dq.popleft(); dq.pop()

# namedtuple：輕量結構
Point = namedtuple("Point", "x y")
p = Point(1, 2); p.x  # 1
```

## 5) heapq（最小堆 / Priority Queue）

```python
import heapq

# 最小堆
h = [5, 1, 3]
heapq.heapify(h)
heapq.heappush(h, 2)
x = heapq.heappop(h)     # 1

# 最大堆：用負數模擬
maxh = []
heapq.heappush(maxh, -5)
heapq.heappush(maxh, -1)
largest = -heapq.heappop(maxh)  # 5

# 取前K大/小（比全排序快）
import heapq
top_k = heapq.nlargest(3, arr)
small_k = heapq.nsmallest(3, arr)
```

## 6) itertools（排列組合等）

```python
from itertools import permutations, combinations, product, accumulate

list(permutations([1,2,3], 2))
list(combinations([1,2,3], 2))
list(product([0,1], repeat=3))         # 所有二進制長度3
prefix_sums = list(accumulate([1,2,3]))  # [1,3,6]
```

## 7) bisect（二分搜尋工具）

```python
import bisect
a = [1, 2, 4, 4, 5]
i = bisect.bisect_left(a, 4)   # 2
j = bisect.bisect_right(a, 4)  # 4
# 插入保持有序
bisect.insort(a, 3)            # a -> [1,2,3,4,4,5]
```

## 8) array（數字專用、省記憶體）

```python
from array import array
a = array('i', [1,2,3])  # 'i' 表 int
a.append(4)
```

## 9) 字串技巧（刷題高頻）

```python
s = "abca"
s[::-1]             # 反轉
s.startswith("ab")  # 前綴
s.endswith("ca")    # 後綴
s.replace("a", "x")
"".join(["a","b","c"])
list("abc")         # -> ['a','b','c']
ord('a'), chr(97)
```

## 10) 排序 sort/sorted（Timsort）

* 複雜度：一般 **O(n log n)**；部分有序時可接近 **O(n)**
* 穩定排序（可多鍵分步排序）
* **效能注意**：`key=` 函式會對每個元素先呼叫一次；若 key 計算昂貴，請先快取或簡化。

```python
arr.sort(key=lambda x: (x.score, x.id))  # 單次多鍵
# 或利用穩定排序分兩次：
arr.sort(key=lambda x: x.id)
arr.sort(key=lambda x: x.score)
```


## 11) 常見題型模板

### A) 兩指針 / Sliding Window

```python
def longest_subarray(arr, condition):
    left = 0
    best = 0
    # 可加入計數器/字典維護狀態
    for right, val in enumerate(arr):
        # 擴窗：更新狀態
        # ...

        # 若不滿足條件 -> 縮窗直至滿足
        while not condition(...):
            # 撤銷 arr[left] 對狀態的影響
            left += 1

        best = max(best, right - left + 1)
    return best
```

### B) 單調棧（下一個更大元素 / 範圍問題）

```python
def next_greater(nums):
    res = [-1]*len(nums)
    st = []  # 存索引，保持遞減（棧頂最小）
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            j = st.pop()
            res[j] = x
        st.append(i)
    return res
```

### C) 前綴和 / 差分

```python
# 前綴和
pre = [0]
for x in arr:
    pre.append(pre[-1] + x)
# 任意區間 [l, r] 和 = pre[r+1] - pre[l]

# 差分：多次區間加法的加速
diff = [0]*(n+1)
# 對 [l, r] 每項 +v
diff[l] += v; diff[r+1] -= v
# 還原
for i in range(1, n):
    diff[i] += diff[i-1]
```

### D) DFS / 回溯

```python
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for nei in graph[node]:
        dfs(nei, visited)

# 回溯（模板）
def backtrack(path, choices):
    if 終止條件:
        ans.append(path[:]); return
    for c in choices:
        # 做選擇
        path.append(c)
        backtrack(path, choices)
        # 撤銷選擇
        path.pop()
```

### E) BFS（最短步數 / 分層）

```python
from collections import deque
def bfs(start):
    q = deque([start])
    dist = {start: 0}
    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist
```

### F) Dijkstra（加權最短路，非負邊）

```python
import heapq
def dijkstra(n, graph, src):
    INF = 10**18
    dist = [INF]*n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d,u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v,w in graph[u]:      # (鄰點, 邊權)
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

### G) Union-Find（並查集 / 連通分量 / Kruskal）

```python
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n            # rank/size

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])  # 路徑壓縮
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb: return False
        # 按秩合併
        if self.r[pa] < self.r[pb]:
            pa, pb = pb, pa
        self.p[pb] = pa
        if self.r[pa] == self.r[pb]:
            self.r[pa] += 1
        return True
```

### H) 最長共同前綴（zip 技巧）

```python
def longestCommonPrefix(strs):
    prefix = []
    for cs in zip(*strs):         # 逐列抓同一位置的字元
        if len(set(cs)) == 1:
            prefix.append(cs[0])
        else:
            break
    return "".join(prefix)
```

### I) 第 K 大元素（避免整體排序）

```python
import heapq

def kth_largest(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]  # k 個中最小者 = 全域第 k 大
```

## 12) 小心陷阱（常考）

```python
# 1) 可變預設參數陷阱
def f(bad=[]):        # ❌ 千萬別這樣
    bad.append(1)
    return bad

def f_good(a=None):   # ✅ 正確
    if a is None:
        a = []
    a.append(1)
    return a

# 2) 浅拷貝 vs 深拷貝
import copy
a = [[1],[2]]
b = a[:]              # 浅拷貝（內層共用）
c = copy.deepcopy(a)  # 深拷貝（完全新物件）

# 3) sort vs heap/quickselect
# - 全部排序 O(n log n)；若只需 Top-K 或第 K 大，優先考慮 O(n log k) 的 heap 或平均 O(n) 的 quickselect
```

## 13) 時間複雜度速覽（常見）

* `list`：index / 更新 O(1)，插入/刪除尾端 O(1)，頭部 O(n)
* `dict`/`set`：平均插入/查找/刪除 O(1)
* `deque`：頭尾推入/彈出 O(1)
* `heapq`：push/pop O(log n)
* `sort/sorted`：O(n log n)，穩定；key 函式成本要注意
