from collections import deque

# 입력값으로 정수 n을 받음
n = int(input())

# n x n 크기의 이차원 리스트를 입력받아 color에 저장
color = [list(input()) for _ in range(n)]

# 너비 우선 탐색을 위한 deque 생성
q = deque()

# 너비 우선 탐색 함수 정의
def bfs(x, y):
    q.append((x, y))
    dx = [1, -1, 0, 0]  # 상하좌우 이동을 위한 dx, dy
    dy = [0, 0, 1, -1]
    visited[x][y] = 1  # 방문한 위치를 표시하는 visited 배열에 해당 위치 방문표시

    while q:
        x, y = q.popleft()

        # 상하좌우 인접한 위치에 대해 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고, 현재 위치와 같은 색이며, 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < n and color[nx][ny] == color[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 해당 위치를 방문했음을 표시
                q.append((nx, ny))  # 큐에 해당 위치 추가

# 방문 여부를 표시하는 visited 배열 초기화
visited = [[0] * n for _ in range(n)]

# 적록색약이 아닌 경우 
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1

# 적록색약일 경우
for i in range(n):
    for j in range(n):
        if color[i][j] == 'G':
            color[i][j] = 'R'

# 방문 여부를 표시하는 visited 배열 초기화
visited = [[0] * n for _ in range(n)]

# 적록색약에 대한 영역 개수 세기
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1

# 결과 출력
print(cnt1, cnt2)
