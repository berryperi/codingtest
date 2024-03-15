# 케이스의 수 입력 
n = int(input())

# n번만큼 반복하여 각 테스트 케이스에 대해 처리
for i in range(n):
    # 사용자로부터 문자열을 입력 받습니다.
    st = str(input())

    # 'O'가 연속으로 나오는 횟수를 세기 위한 변수
    count = 0
    # 총 점수를 저장하기 위한 변수
    total = 0

    # 입력 받은 문자열의 각 문자에 대해 반복
    for j in list(st):
        # 현재 문자가 'O'인 경우
        if j == 'O':
            # 연속된 'O'의 횟수를 증가
            count += 1
            # 현재까지의 연속된 'O'의 횟수만큼 점수를 증가
            total += count
        # 현재 문자가 'X'인 경우
        if j == 'X':
            # 연속된 'O'의 횟수를 초기화
            count = 0
    # 계산된 총 점수를 출력
    print(total)
