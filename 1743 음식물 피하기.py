from collections import deque
import sys

input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = True  
    count = 1  # 처음 음식물 발견 위치도 카운트에 포함

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]  
            ny = y + dy[k] 

            # 다음 좌표가 유효 범위 내에 있고, 방문하지 않았으며, 음식물이 있는 위치인 경우
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and grid[nx][ny] == 1:
                visit[nx][ny] = True
                q.append([nx, ny])
                count += 1  # 연결된 음식물의 크기 증가

    return count  # 하나의 덩어리 크기 반환

n, m, k = map(int, input().split())
grid = [[0] * m for _ in range(n)]  
visit = [[False] * m for _ in range(n)] 

dx = [1, -1, 0, 0]  
dy = [0, 0, 1, -1]  

for _ in range(k):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = 1  # 음식물이 떨어진 위치 기록

maximum = 0  # 최대 음식물 덩어리 크기
for i in range(n):
    for j in range(m):
        if not visit[i][j] and grid[i][j] == 1:
            maximum = max(maximum, bfs(i, j))  # 가장 큰 덩어리 크기 찾기

print(maximum) 
