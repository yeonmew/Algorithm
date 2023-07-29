N,K = map(int,input().split())
arr = []
res = []
for i in range(1,N+1): # 1 ~ N까지의 수
    arr.append(i)


for _ in range(N): # N번 반복
    i = (i + K-1) % len(arr)
    res.append(arr[i])
    arr.pop(i)

print(f"<{', '.join(map(str, res))}>")