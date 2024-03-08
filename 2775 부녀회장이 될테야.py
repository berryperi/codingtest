# 입력값으로 정수를 받음
t = int(input())

# 건물의 층 수 입력
floor = int(input())

# 호실의 수 입력
ho = int(input())

# 초기 층별 사람 수 리스트 생성
f0 = [x for x in range(1, ho+1)]

# 각 층별 사람 수 계산
for k in range(floor):
    for n in range(1, ho):
        # 각 층의 사람 수를 이전 층의 사람 수와 더함
        f0[n] += f0[n-1]

# 최종적으로 가장 높은 층의 사람 수 출력
print(f0[-1])
