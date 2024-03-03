from collections import deque

# 상, 하, 좌, 우, 대각선 방향
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

# BFS 정의
def bfs(x, y):
    q = deque()
    q.append((x, y)) # 현재 좌표를 q에 넣기

    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()  # 현재 좌표를 언패킹

        # 현재 위치에서 8가지 방향으로의 위치를 확인
        for i in range(8):
            nx = x + dx[i]  # 다음 x 좌표
            ny = y + dy[i]  # 다음 y 좌표

            # 맵의 범위를 벗어나지 않고, 다음 위치에 섬이 있는 경우
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 섬을 방문했다고 표시(0으로 변경)
                q.append((nx, ny))  # 다음 위치를 큐에 삽입

# 맵의 너비와 높이 입력
w, h = map(int, input().split())

# 그래프(맵) 초기화
graph = []

# 그래프(맵) 입력 받기
for _ in range(h):
    graph.append(list(map(int, input().split())))

# 섬의 개수를 세기 위한 변수
island = 0
# 그래프 전체를 순회하며 섬 탐색
for i in range(h):
    for j in range(w):
        # 섬의 시작점(값이 1인 위치)을 찾은 경우
        if graph[i][j] == 1:
            island += 1  # 섬의 개수 증가
            bfs(i, j)  # BFS를 이용하여 섬 탐색 및 마킹

# 섬의 총 개수 출력
print(island)
