import sys
import collections
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드 수, 간선 수를 입력받는다.
edges = [] # 모든 간선에 대한 정보를 담는 리스트를 생성한다.
dist = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화한다.

for _ in range(m):# 그래프 생성
    u, v, w = map(int, input().split()) # 노드, 인접 노드, 가중치를 저장한다.
    edges.append((u, v, w))

def bf(start): # 벨만 포드 알고리즘
    dist[start] = 0 # 시작 노드에 대해서 거리를 0으로 초기화한다.
    for i in range(n): # 정점 수만큼 반복한다.
        for j in range(m): # 매 반복 마다 모든 간선을 확인한다.
            node = edges[j][0] # 현재 노드를 받아온다.
            next_node = edges[j][1] # 다음 노드 받아온다.
            cost = edges[j][2] # 가중치를 받아온다.
            # 현재 간선을 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우 바꾼다.
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재한다.
                if i == n-1: # n-1번 이후 반복에도 값이 갱신되면 음수 순환 존재한다.
                    return True
    return False

# 벨만 포드 알고리즘 수행
negative_cycle = bf(1)

if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리를 출력한다.
    for i in range(2, n+1):
        if dist[i] == INF: # 도달할 수 없는 경우 -1을 출력한다.
            print('-1')
        else: # 도달할 수 있는 경우 거리를 출력한다.
            print(dist[i])