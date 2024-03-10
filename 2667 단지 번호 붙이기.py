from collections import deque

# 입력 받기
n = int(input())
grid = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 그리드 생성
for _ in range(n):
    grid.append(list(map(int, input())))

grid_house = []  # 집의 크기를 저장할 리스트

# 너비 우선 탐색(BFS) 함수 정의
def bfs(x, y):
    q = deque()
    q.append((x, y))
    grid[x][y] = 0  # 방문 처리
    cnt = 1  # 현재 집의 크기

    while q:
        x, y = q.popleft()

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그리드 범위 내이고 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                grid[nx][ny] = 0  # 방문 처리
                q.append((nx, ny))
                cnt += 1  # 집의 크기 증가

    grid_house.append(cnt)  # 집의 크기 리스트에 추가

# 모든 그리드에 대해 BFS 수행
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bfs(i, j)

grid_house.sort()  # 집의 크기 리스트를 정렬
print(len(grid_house))  # 집의 개수 출력
for x in grid_house:
    print(x)  # 각 집의 크기 출력
