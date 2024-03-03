from collections import deque

# 입력 받기
n, m = map(int, input().split())

# 그래프 생성
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

# bfs 정의
def bfs(x, y):
    q = deque() # q정의
    q.append((x,y)) # 현재 좌표를 q에 넣기
    
    # 현재 위치가 1이라면 아스크림을 만들 수 없거나 이미 탐색한 공간이므로 false 반환
    if graph[x][y] == 1:
        return False
    
    # 현재 좌표가 포함된 큐만큼 반복
    while q:
        x, y = q.popleft() # 현재 좌표를 언패킹
        graph[x][y] = 1 # 현재 좌표 언패킹과 동시에 1로 변환

        for i in range(len(dx)):
            nx = x + dx[i] # 상우좌하만큼 다음 x좌표
            ny = y + dy[i] # 상우좌하만큼 다음 y좌표 

            # 그래프 틀은 벗어나지 않으면서 좌표의 값이 0이라면 q에 집어넣음
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                q.append((nx, ny))
                
    # 하나의 얼음 덩어리가 완성 되면 true
    return True            

ice = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j) == True: # 완성된 아스크림이 true라면 ice 카운터 증가
            ice += 1   # 아이스크림 갯수 카운트
        
print(ice)

