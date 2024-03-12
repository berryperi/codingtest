import sys

# 사용자 입력
N, K = map(int, input().split())

# 아이템들을 저장할 리스트
items = []

# N개의 아이템 정보를 입력받고 리스트에 저장
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

# 동적 계획법을 위한 리스트
dp = [0 for _ in range(K+1)]

# 각 아이템에 대해 냅색 알고리즘을 수행
for item in items:
    w, v = item

    # 현재 아이템을 포함하여 최대 가치를 갱신
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i], dp[i-w]+v)

# 최종적으로 얻을 수 있는 최대 가치를 출력
print(dp[-1])

# 동적 계획법 리스트를 출력
print(dp)
