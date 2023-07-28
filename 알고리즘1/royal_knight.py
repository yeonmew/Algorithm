# 프로그램명: 왕실의 나이트
# 작성자: yeonmew
# 작성일: 2023.02.12

from timeit import default_timer as timer
from datetime import timedelta

print("좌표를 입력하세요.")
coordinate = input()# 좌표를 입력받는다.

start_time = timer()
x = int(ord(coordinate[0])-(ord('a')))+1# a=1, b=2,,,로 만든다.
y = int(coordinate[1])

move = [(-1,-2),(-1,2),(1,2),(1,-2),(-2,-1),(-2,1),(2,-1),(2,1)] # 경우의 수를 입력해둔다.
result = 0

for moving in move:
    x_move = x + moving[0]
    y_move = y + moving[1]
    if x_move >= 1 and x_move <= 8 and y_move >= 1 and y_move <= 8:
        result += 1

end_time = timer()
print("경우의 수:",result, ", 걸린 시간:",timedelta(seconds= end_time - start_time))
