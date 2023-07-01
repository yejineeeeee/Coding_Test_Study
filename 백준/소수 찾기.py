N = int(input())  # 정수 N을 입력 받음
cnt = 0  # 소수의 개수를 세는 변수 초기화
num = map(int, input().split())  # N개의 정수를 입력 받아서 num에 저장

for i in num:  # num에 있는 각 정수에 대해 반복
    for j in range(2, i+1):  # 2부터 i까지의 수에 대해 반복
        if i % j == 0:  # i가 j로 나누어 떨어지면 (즉, j가 i의 약수이면)
            if i == j:  # i와 j가 같으면 (즉, i가 소수이면)
                cnt += 1  # cnt를 1 증가시킴

            break  # 첫 번째 약수를 찾았으므로 반복 종료

print(cnt)  # 소수의 개수 출력
