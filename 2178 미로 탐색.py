from collections import deque  

n, m = map(int, input().split())  

graph = []  
for _ in range(n):  
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]  
dy = [0, 0, -1, 1]  


def bfs(x, y): 
    q = deque()  
    q.append((x, y))  

    while q:  
        x, y = q.popleft()  

        for i in range(4):  
            nx = x + dx[i]  
            ny = y + dy[i]  

            # 새로운 좌표가 그래프의 범위 내에 있고, 해당 위치가 1인 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1  # 최단 거리를 구하기 위해 이전 좌표의 값에 1을 더한 값을 새로운 좌표에 할당
                q.append((nx, ny))  # 새로운 좌표를 deque에 추가

    return graph[n-1][m-1]  # 도착 좌표에 해당하는 값을 반환

print(bfs(0, 0))  # bfs 함수를 호출하여 출발 좌표 (0, 0)에서 출구 좌표까지의 최단 경로의 길이를 출력
