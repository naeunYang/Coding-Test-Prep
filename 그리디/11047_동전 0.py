import sys

n, k = list(map(int, sys.stdin.readline().split()))
coins = [int(sys.stdin.readline()) for _ in range(n)]

result = 0

for coin in reversed(coins):
    if coin <= k:
        result += k // coin
        k %= coin

print(result)

# => 메모리: 32412KB, 시간: 44ms, 코드 길이: 238B