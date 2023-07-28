# 프로그램명: 두 배열의 원소 교체
# 작성자: yeonmew
# 작성일: 23.02.15


n,k = map(int, input().split()) # N,K를 입력받는다. 
a = list(map(int, input().split())) # 배열 a를 입력받는다.
b = list(map(int, input().split())) # 배열 b를 입력받는다.

a.sort() # 배열 a는 오름차순 정렬한다.
b.sort(reverse = True) # 배열 B는 내림차순 정렳ㄴ다.

#두 배열의 원소를 최대 K번 비교한다.
for i in range(k):
    # A의 원소가 b의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체한다.
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 b의 원소보다 크거나 같을 때, 중단한다.
        break

print(sum(a)) # 배열 A의 모든 원소의 합을 출력한다.


