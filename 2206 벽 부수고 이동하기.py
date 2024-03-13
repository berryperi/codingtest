from collections import deque

# 입력 받기
n, m = map(int, input().split())
graph = []

# 그래프 생성
for _ in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 방문 여부를 체크할 리스트 (벽을 부수지 않은 경우와 부순 경우로 나눔)
visit = [[[0]*2 for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    # 시작 지점 추가 (x, y, 벽을 부순 횟수)
    q.append((0, 0, 0))
    # 시작 지점을 방문했음을 체크
    visit[0][0][0] = 1

    while q:
        x, y, z = q.popleft()

        # 목적지에 도달했을 경우 거리 반환
        if x == n-1 and y == m-1:
            return visit[x][y][z]

        # 상하좌우 이동 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 범위 내에 있을 때만 탐색
            if 0 <= nx < n and 0 <= ny < m:
                # 다음 위치가 이동 가능한 경우 (벽을 부수지 않은 경우)
                if graph[nx][ny] == 0 and visit[nx][ny][z] == 0:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    q.append((nx, ny, z))
                # 다음 위치가 벽인 경우 (벽을 아직 부순 적이 없는 경우)
                elif graph[nx][ny] == 1 and z == 0:
                    visit[nx][ny][z+1] = visit[x][y][z] + 1
                    q.append((nx, ny, z+1))
    # 도달할 수 없는 경우
    return -1

# 최단 거리 출력
print(bfs())
