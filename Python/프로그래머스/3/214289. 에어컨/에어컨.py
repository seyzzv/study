def solution(temperature, t1, t2, a, b, onboard):
    INF = float('inf')
    offset = 10
    dp = [INF] * 51
    dp[temperature + offset] = 0

    for i in range(1, len(onboard)):
        ndp = [INF] * 51

        for temp in range(-10, 41):
            cost = dp[temp + offset]
            if cost == INF:
                continue

            if temp == temperature:
                ndp[temp + offset] = min(ndp[temp + offset], cost)
            else:
                next_temp = temp + (1 if temperature > temp else -1)
                if -10 <= next_temp <= 40:
                    ndp[next_temp + offset] = min(
                        ndp[next_temp + offset], cost
                    )

            ndp[temp + offset] = min(ndp[temp + offset], cost + b)

            for next_temp in (temp - 1, temp + 1):
                if -10 <= next_temp <= 40:
                    ndp[next_temp + offset] = min(
                        ndp[next_temp + offset], cost + a
                    )

        if onboard[i]:
            for temp in range(-10, 41):
                if not t1 <= temp <= t2:
                    ndp[temp + offset] = INF

        dp = ndp

    return min(dp)