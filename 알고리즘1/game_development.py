# 프로그램명: 게임 개발
# 작성자: yeonmew
# 작성일: 2023.02.13 

from timeit import default_timer as timer
from datetime import timedelta

N,M = map(int, input().split()) # N x M의 맵

c = [[0] * M for _ in range(N)] # 방문 위치 저장을 위한 맵 생성

x, y, direction = map(int,input().split()) # 현재 캐릭터의 x, y좌표와 방향 입력 
c[x][y] = 1 # 현 좌표 방문 처리

arr = []
for _ in range(N): #맵 입력
    arr.append(list(map(int, input().split())))

start_time = timer()

dx = [-1,0,1,0] # 방향 정의
dy = [0,1,0,-1]

def turn_left(): #왼쪽으로 회전
    global direction
    direction -= 1 
    if direction == -1:
        direction = 3

count = 1
turn_count = 0

while True:
    turn_left()
    cx = x + dx[direction] 
    cy = y + dy[direction]

    if c[cx][cy] == 0 and arr[cx][cy] == 0: # 회전 후 정면으로 갈 수 있는 경우
        c[cx][cy] = 1
        x = cx # 현재 위치 x를 이동 예정인 방향 cx로 이동
        y = cy
        count += 1
        turn_count = 0
        continue
    else: # 회전 후 정면으로 갈 수 없는 경우
        turn_count += 1

    if turn_count == 4:
        cx = x - dx[direction]
        cy = y - dy[direction]
        
        if arr[cx][cy] == 0: # 뒤로 갈 수 있다면 이동
            x = cx
            y = cy
        else: # 뒤로 이동할 수 없는 경우
            break
        turn_count = 0
end_time = timer()

print(count, timedelta(seconds= end_time - start_time))

    
