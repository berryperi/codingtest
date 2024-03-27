from collections import deque

N = int(input())
grid = [[] for _ in range(N+1)]

def bfs(n):
    visited = [-1] * (N+1)
    visited[n] = 0
    q = deque([n])
    while q:
        v = q.popleft()
        for w in grid[v]:
            if visited[w] == -1:
                visited[w] = visited[v] + 1
                q.append(w)
    return max(visited)


while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    grid[a].append(b)
    grid[b].append(a)

score = 50
lst = []

for n in range(1, N+1):
    tmp = bfs(n)
    if tmp < score:
        score = tmp
        lst = [n]
    elif tmp == score:
        lst.append(n)
print(score, len(lst))
print(*lst)