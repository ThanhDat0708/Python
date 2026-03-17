from collections import deque

tree={
    1:[2,3,4],
    2:[5,6],
    3:[],
    4:[7,8,9],
    5:[],
    6:[10,11],
    7:[11],
    8:[12,13],
    9:[13,14],
    10:[],
    11:[],
    12:[],
    13:[],
    14:[],
}
# bfs
def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited.append(node)
        queue.extend(tree[node])
    
    return visited
print(bfs(1))