import turtle as t
import time

# 5초에 한번씩 함수 실행
# 무지개 반원
# 꽃꽃

n = 5
t.pencolor = 'yellow'
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right((360 / n) * 2)
    t.forward(100)
    t.left(360 / n)