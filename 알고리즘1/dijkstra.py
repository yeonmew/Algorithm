graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq  # 우선순위 큐 구현

def dijkstra(graph, start):
  distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장한다.
  distances[start] = 0  # 시작 값은 0이어야 한다.
  queue = []
  heapq.push(queue, [distances[start], start])  # 시작 노드부터 탐색을 시작한다.

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드와 거리를 가져온다.

    if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길면 확인하지 않는다.
      continue
    
    for new_destination, new_distance in graph[current_destination].items():
      distance = current_distance + new_distance  # 해당 노드를 거쳐 가는 거리를 계산한다.
      if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 수정한다.
        distances[new_destination] = distance
        heapq.push(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입한다.
    
  return distances