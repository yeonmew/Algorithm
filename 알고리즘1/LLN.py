# 프로그램명: 큰 수의 법칙
# 작성자: yeonmew
# 작성일: 23.02.02

from timeit import default_timer as timer
from datetime import timedelta

print("N, M, K를 입력하세요.")
N,M,K = map(int, input().split())  #배열의 크기 N, 총 몇번 더하는지 M, 최대 몇번까지 더하는지 K
print(N,"개의 자연수를 입력하세요.")
arr = list(map(int, input().split()))

result = 0

start_time = timer()

arr.sort(reverse=True) # 내림차순으로 정렬한다.
for j in range(0, M):
    if M < K:
        result += arr[0]*M # K가 M보다 작으니, 남은 덧셈 횟수인 M번만큼만 더한다.
        break

    else:
        result += arr[0]*K # 가장 큰 수를 연속해서 더할 수 있는 최대인 K번 더한다.
        M -= K # K번 더했으니, 총 덧셈 횟수 M에서 K를 뺀다.
        result += arr[1] # 두번째로 큰 수를 1번 더한다.
        M -= 1

end_time = timer()

print("큰 수의 법칙 결과: ",result)
print("실행 시간: ", timedelta(seconds = end_time - start_time))