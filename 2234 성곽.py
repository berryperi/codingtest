from collections import deque

n, m = map(int, input().split())
grid = []  # 성의 구조를 저장할 리스트

# m번 반복하여 성의 각 행에 대한 정보를 입력받음
for _ in range(m):
    grid.append(list(map(int, input().split())))

# 남, 동, 북, 서
four = [8, 4, 2, 1]

#남동북서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

room = 0  # 방의 총 수
group_num = 0  # 방의 고유 번호

visit = [[0] * n for _ in range(m)]

# 각 칸에 대한 방 정보(방 번호와 크기)
room_info = [[[] for _ in range(n)] for _ in range(m)]

def bfs(x, y):
    global group_num  # 전역 변수 group_num 사용 선언

    visit[x][y] = 1  # 시작점 방문 처리

    q = deque()  
    q.append((x, y))

    area = 1  # 방의 크기 초기화

    group = []  # 현재 방을 이루는 칸
    group.append((x, y))

    while q:
        px, py = q.popleft()
        wall = grid[px][py]  # 현재 칸의 벽 정보
        for i in range(4):
            if wall >= four[i]:
                wall -= four[i]  # 벽이 있으면 벽 값을 감소시킴
            else:
                nx, ny = px + dx[i], py + dy[i]

                # 인접 칸이 범위 내에 있고 미방문 상태일 경우
                if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny]:  
                    area += 1
                    q.append((nx, ny))
                    visit[nx][ny] = 1
                    group.append((nx, ny))

    for i, j in group:
        room_info[i][j].append(group_num)  # 방 번호 저장
        room_info[i][j].append(area)  # 방 크기 저장

    group_num += 1  # 다음 방 번호 증가

    return area

room_max = 0  # 가장 큰 방의 크기
for i in range(m):
    for j in range(n):
        if not visit[i][j]:  # 방문하지 않은 칸에서 BFS 시작
            room_max = max(bfs(i, j), room_max)
            room += 1  # 방의 개수 증가

sub_max = 0  # 벽을 제거하여 얻을 수 있는 가장 큰 방의 크기
for i in range(m):
    for j in range(n):
        for d in range(4):
            if grid[i][j] >= four[d]:  # 벽이 있는 경우
                nx, ny = i + dx[d], j + dy[d]

                if 0 <= nx < m and 0 <= ny < n:
                    if room_info[i][j][0] != room_info[nx][ny][0]:  # 서로 다른 방인 경우
                        sub_max = max(sub_max, room_info[i][j][1] + room_info[nx][ny][1])  # 두 방 크기의 합을 최대값과 비교

print(room)
print(room_max)
print(sub_max)
