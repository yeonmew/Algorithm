# 프로그램명: 큰 수의 법칙 ver.2
# 작성자: yeonmew
# 작성일: 23.02.04

from timeit import default_timer as timer
from datetime import timedelta

print("N, M, K를 입력하세요.")
N,M,K = map(int, input().split())  #배열의 크기 N, 총 몇번 더하는지 M, 최대 몇번까지 더하는지 K
print(N,"개의 자연수를 입력하세요.")
arr = list(map(int, input().split()))

result = 0

start_time = timer()

arr.sort(reverse=True) # 내림차순으로 정렬한다.

count = M // (K+1) * K  # 가장 큰 수가 더해지는 횟수를 계산한다.
count += M % (K+1)

result = count * arr[0] # 가장 큰 수를 더한다.
result += (M - count) * arr[1] # 두번째로 큰 수를 더한다.

end_time = timer()

print("큰 수의 법칙 결과: ",result)
print("실행 시간: ", timedelta(seconds = end_time - start_time))