book = dict()
res = []

for _ in range(int(input())): # 책 개수 N
    x = input()
    if x in book:
        book[x] += 1
    else:
        book[x] = 1

for b_name, count in book.items():
    if count == max(book.values()):
        res.append(b_name)

res.sort()

print(res[0])