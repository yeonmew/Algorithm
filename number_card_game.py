# 프로그램명: 숫자 카드 게임
# 작성자: yeonmew
# 작성일: 23.02.04

from timeit import default_timer as timer
from datetime import timedelta

print("행 N, 열 M을 입력해주세요.")
N, M = map(int, input().split())

arr1 = []
print(N," x ",M,"의 숫자를 입력해주세요.")

for _ in range(N): #arr 리스트에 배열을 저장하고, 그 중 최소를 찾는다.
    arr = list(map(int, input().split()))
    arr1.append(min(arr))

start_time = timer()
print("카드에 적힌 숫자: ", max(arr1))
end_time = timer()
print("실행 시간: ", timedelta(seconds= end_time - start_time))

