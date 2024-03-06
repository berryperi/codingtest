from collections import deque

# bfs 함수: 시작점을 받아서 인접한 "-"이나 "|"를 찾아내고 방문표시("1")
def bfs(x, y):
    q = deque()  
    q.append((x, y))  

    while q:  
        x, y = q.popleft()  
        
        # 현재 위치의 판자가 "-"인 경우
        if gra[x][y] == "-":
            gra[x][y] = "1"  # 방문표시

            # 오른쪽에 "-"가 있으면 큐에 추가
            if y+1 < m and gra[x][y+1] == "-":
                q.append((x, y+1))

        # 현재 위치의 판자가 "|"인 경우
        elif gra[x][y] == "|":
            gra[x][y] = "1"  # 방문표시
            
            # 아래쪽에 "|"가 있으면 큐에 추가
            if x+1 < n and gra[x+1][y] == "|":
                q.append((x+1, y))
            
# 입력
n, m = map(int, input().split())  
gra = [list(input()) for _ in range(n)]  # 판자 정보
wood = 0  # 방문할 판자 개수

# 모든 판자에 대해 bfs 실행
for i in range(n):
    for j in range(m):
        if gra[i][j] != "1":  # 방문하지 않은 판자라면
            bfs(i, j)  
            wood += 1  # 판자 개수 증가

print(wood)  # 결과 출력