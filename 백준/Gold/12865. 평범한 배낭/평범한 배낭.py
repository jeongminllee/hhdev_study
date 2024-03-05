n, k = map(int, input().split())
items = [[0, 0]]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for _ in range(n) :
    items.append(list(map(int, input().split())))

for i in range(1, n + 1) :
    for j in range(1, k + 1) :
        w = items[i][0]
        p = items[i][1]

        if j < w :
            dp[i][j] = dp[i - 1][j]

        else :
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + p)

print(dp[n][k])