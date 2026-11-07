def solution(n):
    arr = [[0] * n for _ in range(n)]
    num = 1
    x, y = 0, 0

    dx = [1, 0, -1]
    dy = [0, 1, -1]

    direction = 0

    for _ in range(n * (n + 1) // 2):
        arr[x][y] = num
        num += 1

        nx = x + dx[direction]
        ny = y + dy[direction]

        if (nx < 0 or nx >= n or
            ny < 0 or ny >= n or
            arr[nx][ny] != 0):

            direction = (direction + 1) % 3

            nx = x + dx[direction]
            ny = y + dy[direction]

        x, y = nx, ny

    answer = []

    for i in range(n):
        answer.extend(arr[i][:i + 1])

    return answer