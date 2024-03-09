# 정수 입력 받기
n = int(input())

# n번 반복
for i in range(n):
    # 문자열 입력 받기
    st = str(input())

    # 'O'의 연속된 개수를 세는 변수 count와 총합을 저장할 변수 total 초기화
    count = 0
    total = 0

    # 문자열을 하나씩 탐색
    for j in list(st):
        # 현재 문자가 'O'인 경우
        if j == 'O':
            count += 1  # 연속된 'O'의 개수 증가
            total += count  # 총합에 현재 연속된 'O'의 개수를 더함
        # 현재 문자가 'X'인 경우
        if j == 'X':
            count = 0  # 연속된 'O'의 개수 초기화
    # 한 테스트 케이스에 대한 총합 출력
    print(total)
