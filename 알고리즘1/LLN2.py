# 프로그램명: 큰 수의 법칙
# 작성자: yeonmew
# 작성일: 23.01.29

# 첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 
# 자연수가 주어지며 각자연수는 공백으로 구분한다.
print("N, M, K를 입력하세요.")
N,M,K = map(int, input().split())  #배열의 크기 N, 총 몇번 더하는지 M, 최대 몇번까지 더하는지 K
# 둘째 줄에 N개의 자연수가 주어진다. 
# 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000 이하의 수로 주어진다.
arr = [] 
print(N,"개의 자연수를 입력하세요.")
arr = list(map(int, input().split()))

result = 0
i = 0
arr.sort(reverse=True) # 내림차순으로 정렬한다.

for j in range(0, M):
    if M < K:
        result += arr[i]*M # K가 M보다 작으니, 남은 덧셈 횟수인 M번만큼만 더한다.
        break

    else:
        result += arr[i]*K # K번 더한다.
        i += 1 # 인덱스를 옮겨준다.
        M -= K # K번 더했으니, 총 덧셈 횟수 M에서 K를 뺀다.

print("큰 수의 법칙 결과: ",result)