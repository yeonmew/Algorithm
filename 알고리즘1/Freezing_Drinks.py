# 프로그램명: 음료 얼려먹기
# 작성자: yeonmew
# 작성일: 2023.02.13 

from timeit import default_timer as timer
from datetime import timedelta

N,M = map(int,input().split())

#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(N):
    graph.append(list(map(int,input())))

start_time = timer()
#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    #현재 아직 노드를 방문하지 않았다면 
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        #상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs(x -1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

#모든 노드에 대해 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        #현재 위치에서 DFS수해
        if dfs(i,j) == True:
            result += 1
end_time = timer()

print(result, timedelta(seconds=end_time - start_time)) #정답 출력