n, k = map(int, input().split())
cat = list(map(int, input().split()))
c1, c2 = 0, n-1

# 고양이의 무게를 정렬
cat.sort()

happy = 0

# 투 포인터가 서로 교차하기 전까지 반복
while c1 < c2:
    # c1번째 고양이와 c2번째 고양이의 무게 합이 K 이하인 경우,
    # 두 고양이를 한 사람에게 할당하고 두 포인터를 조절
    if cat[c1] + cat[c2] <= k:
        c1 += 1
        c2 -= 1
        happy += 1
    # 무게 합이 K를 초과하는 경우, c2번째 고양이가 너무 무거운 것이므로
    # c2 포인터만 조절하여 다음으로 무거운 고양이를 확인
    else:
        c2 -= 1
    
print(happy)
