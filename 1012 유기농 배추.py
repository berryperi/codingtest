from collections import deque

# BFS 함수 정의
def bfs(x, y):
    q = deque()  # 큐 생성
    q.append((x, y))  # 시작 지점을 큐에 추가

    # BFS 수행
    while q:
        x, y = q.popleft()  # 큐에서 좌표를 하나 꺼내옴
        graph[x][y] = 0  # 해당 좌표를 방문했음을 표시

        # 상하좌우
        for i in range(4):
            nx = x + dx[i]  # 새로운 x 좌표
            ny = y + dy[i]  # 새로운 y 좌표

            # 새로운 좌표가 그래프 내에 있고, 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))  # 큐에 새로운 좌표 추가
                graph[nx][ny] = 0  # 해당 좌표를 방문했음을 표시

# 테스트 케이스의 개수
t = int(input())

# 상하좌우
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 각 테스트 케이스에 대해 수행
for _ in range(t):
    # 세로(n), 가로(m), 배추 개수(k)를 입력 받음
    m, n, k = map(int, input().split())

    # 그래프 초기화
    graph = [[0] * m for _ in range(n)]

    # 배추의 위치를 그래프에 표시
    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    worm = 0  # 지렁이 수 초기화
    # 모든 좌표에 대해 탐색하면서 배추가 심어져 있는 경우 BFS 수행
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)  # BFS 수행
                worm += 1  # 지렁이 수 증가

# 최종 결과 출력
print(worm)