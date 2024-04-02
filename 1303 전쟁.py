from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
visited = [[False] * n for i in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, color):
    cnt = 0    # 현재 탐색 중인 병사 그룹의 크기를 저장할 변수
    queue = deque()    # BFS 탐색을 위한 큐
    queue.append((x, y))    # 현재 병사의 위치를 큐에 추가
    visited[x][y] = True    # 현재 병사의 위치를 방문 처리

    while queue:
        x, y = queue.popleft()    # 큐에서 병사의 위치를 꺼냄

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 탐색 위치가 격자 안에 있고, 같은 색의 병사이며, 아직 방문하지 않았다면
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True    # 방문 처리
                    queue.append((nx, ny))    # 큐에 추가
                    cnt += 1    # 그룹 크기 증가

    return cnt + 1    # 처음 탐색 시작한 병사 포함하여 반환

# 아군과 적군의 위력 합계 초기화
white, blue = 0, 0
# 모든 격자를 순회하며 BFS 탐색
for i in range(m):
    for j in range(n):
        # 흰색 병사를 만났고, 아직 방문하지 않았다면
        if graph[i][j] == 'W' and not visited[i][j]:
            white += bfs(i, j, 'W') ** 2    # 아군 병사의 위력 계산 및 누적
        # 파란색 병사를 만났고, 아직 방문하지 않았다면
        elif graph[i][j] == 'B' and not visited[i][j]:
            blue += bfs(i, j, 'B') ** 2    # 적군 병사의 위력 계산 및 누적

# 최종 계산된 아군과 적군의 위력 합계 출력
print(white, blue)