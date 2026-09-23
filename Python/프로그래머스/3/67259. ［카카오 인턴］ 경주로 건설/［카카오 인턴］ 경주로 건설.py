import heapq


def solution(board):
  n = len(board)
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]

  costs = [[[float("inf")] * 4 for _ in range(n)] for _ in range(n)]

  q = []
  heapq.heappush(q, (0, 0, 0, -1))

  while q:
    cost, x, y, d = heapq.heappop(q)

    if x == n - 1 and y == n - 1:
      return cost

    if d != -1 and costs[x][y][d] < cost:
      continue

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 1:
        continue

      if d == -1:
        new_cost = 100
      elif d == i:
        new_cost = cost + 100
      else:
        new_cost = cost + 600

      if new_cost < costs[nx][ny][i]:
        costs[nx][ny][i] = new_cost
        heapq.heappush(q, (new_cost, nx, ny, i))

  return 0