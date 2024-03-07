from itertools import combinations  
from collections import deque  
import copy

graph = []  # 그래프 초기화
wall = []  # 벽의 위치 초기화
virus = []  # 바이러스의 위치 초기화

# 상하좌우
dx = [1, -1, 0, 0]  
dy = [0, 0, 1, -1]  

def bfs():  
    q = deque(virus)  
    testgraph = copy.deepcopy(graph)  # 테스트용 그래프 생성

    while q:  
        x, y = q.popleft()  
        for i in range(4):  
            nx = x + dx[i]  
            ny = y + dy[i]  

            if 0 <= nx < n and 0 <= ny < m and testgraph[nx][ny] == 0:  # 새로운 위치가 그래프 안에 있고, 빈 공간인 경우
                testgraph[nx][ny] = 2  # 해당 위치에 바이러스 전파 표시
                q.append((nx, ny))  

    count = 0  # 빈 공간의 개수 초기화
    for i in range(n):  # 모든 행에 대해 반복
        for j in range(m):  # 각 행의 모든 열에 대해 반복
            if testgraph[i][j] == 0:  # 빈 공간인 경우
                count += 1  # 빈 공간 개수 증가

    return count  # 빈 공간 개수 반환

n, m = map(int, input().split())  # 행과 열의 개수 입력 받기

for i in range(n):  # 모든 행에 대해 반복
    graph.append(list(map(int, input().split())))  # 각 행의 정보 입력 받아 그래프에 추가

    for j in range(m):  # 각 행의 모든 열에 대해 반복
        if graph[i][j] == 0:  # 빈 공간인 경우
            wall.append((i, j))  # 벽 리스트에 추가
        if graph[i][j] == 2:  # 바이러스인 경우
            virus.append((i, j))  # 바이러스 리스트에 추가

maxwall = 0  # 최대 벽의 개수 초기화
for data in combinations(wall, 3):  # 벽의 조합에 대해 반복
    for x, y in data:  # 각 벽의 좌표에 대해 반복
        graph[x][y] = 1  # 해당 위치에 벽을 설치

    maxwall = max(maxwall, bfs())  # 최대 벽 개수 갱신

    for x, y in data:  # 벽 설치한 곳을 다시 빈 공간으로 만들기 위해 반복
        graph[x][y] = 0  # 해당 위치의 벽 제거

print(maxwall)  # 최대벽 개수 출력
