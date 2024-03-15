import sys
from collections import deque

# 도시 수(N), 도로 수(M), 거리 정보(K), 출발 도시(X)
input = sys.stdin.readline
N, M, K, X = map(int, input().split())

# 그래프를 인접 리스트 형태로 초기화. N+1은 0번 인덱스를 사용하지 않음
graph = [[] for _ in range(N+1)]

# 각 도시까지의 최단 거리를 저장할 리스트를 -1(방문하지 않음)으로 초기화
distance = [-1] * (N+1)

# 출발 도시 X까지의 거리는 0으로 설정
distance[X] = 0

# 모든 도로 정보를 입력받아 그래프에 저장
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# BFS를 위한 큐를 초기화하고 출발 도시 X를 넣음
q = deque([X])
while q:
    now = q.popleft()

    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next] == -1:
            # 현재 도시까지의 거리 + 1을 해서 거리를 갱신하고 큐에 넣음
            distance[next] = distance[now]+1
            q.append(next)

# 거리가 K인 모든 도시를 출력
check = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True

# 거리가 K인 도시가 없다면 -1을 출력
if not check:
    print(-1)
