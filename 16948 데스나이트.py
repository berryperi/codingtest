import sys
from collections import deque

def bfs():
    queue = deque()  
    queue.append([r1, c1])  
    visit[r1][c1] = 1  

    while queue:
        a, b = queue.popleft()  

        for i in range(6):  
            x = a + dx[i]  
            y = b + dy[i]

            if 0 <= x < g and 0 <= y < g and visit[x][y] == 0:  # 새 위치가 체스판 내부이고 아직 방문하지 않았다면
                visit[x][y] = visit[a][b] + 1  # 이동 횟수 갱신
                queue.append((x, y))  # 새 위치를 큐에 추가

g = int(sys.stdin.readline())  # 체스판의 크기 g 입력

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())  # 시작 위치 (r1, c1)과 목표 위치 (r2, c2) 입력
dx = [-2, -2, 0, 0, 2, 2]  # 데스 나이트의 x축 이동
dy = [-1, 1, -2, 2, -1, 1]  # 데스 나이트의 y축 이동

visit = [[0] * g for _ in range(g)]  # 방문 및 이동 횟수 기록을 위한 2차원 배열 초기화

bfs()  # 너비 우선 탐색 실행

# 결과 출력
if visit[r2][c2] == 0:
    print(-1)  # 목표 위치에 도달하지 못한 경우 -1 출력
else:
    print(visit[r2][c2] - 1)  # 목표 위치에 도달한 경우, 최소 이동 횟수 출력 (시작 위치의 거리를 1로 초기화했으므로 -1 조정)