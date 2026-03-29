from collections import deque

tree={
    1:[2,3,4],
    2:[5,6],
    3:[],
    4:[7,8,9],
    5:[],
    6:[10,11],
    7:[],
    8:[12,13],
    9:[14],
    10:[],
    11:[],
    12:[],
    13:[],
    14:[],
}
# bfs
# bfs là thuật toán duyệt theo chiều rộng, sử dụng hàng đợi để lưu trữ các node cần duyệt
# deque là một cấu trúc dữ liệu cho phép thêm và xóa phần tử ở cả hai đầu, nhưng ở đây chúng ta chỉ sử dụng nó như một hàng đợi (queue) bằng cách thêm phần tử vào cuối và xóa phần tử từ đầu
def bfs(start):
    visited = []
    queue = deque([start])
# popleft là xóa và trả về phần tử đầu tiên của hàng đợi
    while queue:
        node = queue.popleft()
        visited.append(node)
        queue.extend(tree[node])
    
    return visited
print(f"bfs: {bfs(1)}")
# dfs
def dfs(start):
    visited = []
    stack = [start]
# pop là xóa và trả về phần tử cuối cùng của ngăn xếp
    while stack:
        node = stack.pop()
        visited.append(node)
        stack.extend(tree[node])
    
    return visited
print(f"dfs: {dfs(1)}")