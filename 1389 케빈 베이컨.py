from collections import deque

# 입력값으로 노드의 수(n)와 간선의 수(m)을 받음
n, m = map(int, input().split())
# 친구 관계를 저장할 이차원 리스트를 생성
friend = [[] for i in range(n+1)]

# 친구 관계를 입력받음
for i in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

# 너비 우선 탐색 함수 정의
def bfs(start):
    # 큐 생성
    q = deque()
    # 시작 노드를 큐에 추가
    q.append(start)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 현재 노드를 꺼냄
        now = q.popleft()

        # 현재 노드와 연결된 노드들을 확인
        for next_man in friend[now]:
            # 방문하지 않은 노드이고, 시작 노드와 같은 노드가 아닌 경우
            if visit[next_man] == 0 and start != next_man:
                # 방문 표시 및 거리 계산
                visit[next_man] = visit[now] + 1
                # 다음 노드를 큐에 추가
                q.append(next_man)

# 최종 결과를 저장할 변수 초기화
result = float('inf')

# 모든 노드에 대해 최소 거리 계산
for i in range(1, n+1):
    # 각 노드를 시작점으로 하여 bfs 실행
    visit = [0 for i in range(n+1)]
    
    bfs(i)
    # 케빈 베이컨의 수 계산
    kevin = sum(visit)

    # 현재 결과와 비교하여 최소값 갱신
    if kevin < result:
        result = kevin
        min_kevin = i

# 최소 케빈 베이컨의 수를 출력
print(min_kevin)
# 최소 케빈 베이컨의 수 출력
print(result)
