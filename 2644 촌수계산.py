from collections import deque

n = int(input()) 
a, b = map(int,input().split()) 

def bfs(start):
    q = deque()
    q.append(start)

    result[start] = 0

    while q:
        now = q.popleft()

        for i in graph[now]: # 연결된 노드 확인
            
            if result[i] == -1: # 아직 초기값이라면
                result[i] = result[now] + 1 # 현재 노드값에 1을 더해 갱신
                q.append(i)   # 큐에 삽입

graph = [[] for _ in range(n + 1)] # 관계 그래프
result = [-1] * (n + 1) # 촌수를 저장할 list
m = int(input()) # 관계의 개수

for _ in range(m):
    x, y = map(int,input().split()) # 부모, 자식
    graph[x].append(y) # 양방향으로 연결
    graph[y].append(x)

bfs(a)
if result[b] == -1: # 수행한 결과 아직 초기값이라면
    print(-1)       # -1 출력
else:
    print(result[b])