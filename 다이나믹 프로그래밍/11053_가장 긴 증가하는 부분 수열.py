import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# => 메모리: 32412KB, 시간: 124ms, 코드 길이: 247B