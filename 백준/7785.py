import sys

input = sys.stdin.readline

출입 = dict()
res = []

for _ in range(int(input())): 
    x, y = map(str, input().split())
    출입[x] = y

for x, y in 출입.items():
    if y == 'enter':
        res.append(x)

res.sort(reverse=True)

for i in range(len(res)):
    print(res[i])