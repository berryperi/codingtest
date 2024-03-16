# 입력 받기
n = int(input())  # 숫자의 개수
num = list(map(int, input().split()))  # 숫자들
op = list(map(int, input().split()))   # 연산자 개수

# 최대값과 최소값 초기화
maximum = -1e9
minimum = 1e9

# 깊이 우선 탐색 함수 정의
def dfs(dep, total, plus, sub, mul, div):
    global maximum, minimum
    
    # 기저 사례: 모든 숫자에 대한 연산이 완료된 경우
    if dep == n:
        maximum = max(total, maximum)  # 최대값 갱신
        minimum = min(total, minimum)  # 최소값 갱신
        return

    # 덧셈 연산자가 남아있는 경우
    if plus:
        dfs(dep+1, total+num[dep], plus-1, sub, mul, div)
    # 뺄셈 연산자가 남아있는 경우
    if sub:
        dfs(dep+1, total-num[dep], plus, sub-1, mul, div)
    # 곱셈 연산자가 남아있는 경우
    if mul:
        dfs(dep+1, total*num[dep], plus, sub, mul-1, div)
    # 나눗셈 연산자가 남아있는 경우
    if div:
        dfs(dep+1, int(total/num[dep]), plus, sub, mul, div-1)            

# 초기 호출
dfs(1, num[0], op[0], op[1], op[2], op[3])

# 결과 출력
print(maximum)  # 최대값 출력
print(minimum)  # 최소값 출력
