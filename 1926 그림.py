from collections import deque

n, m = map(int, input().split())
graph = []
 
for i in range(n):
    graph.append(list(map(int, input().split())))
 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
 
def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0 # 방문한 노드를 0으로 마킹
    count = 1 # 연결된 영역의 크기
 
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 이동한 위치가 칠해진 영역이라면
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 방문 처리
                queue.append((nx, ny)) # 새 위치를 큐에 삽입
                count += 1 # 영역의 크기 증가
    return count # 영역의 크기 반환
 
paint = [] 
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: # 칠해진 영역이면
            paint.append(bfs(graph, i, j)) # BFS 수행 후 결과를 리스트에 추가
 
# 출력 부분
if len(paint) == 0: # 칠해진 영역이 없으면
    print(len(paint)) # 0 출력
    print(0)
else: # 칠해진 영역이 있으면
    print(len(paint)) # 영역의 수 출력
    print(max(paint)) # 가장 큰 영역의 크기 출력
