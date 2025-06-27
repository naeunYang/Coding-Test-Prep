import sys

t = int(sys.stdin.readline())
changes = [int(sys.stdin.readline()) for _ in range(t)]

coins = [25, 10, 5, 1]

for i in changes:
    array = []
    for j in coins:
        cnt = 0
        if i >= j:
            cnt += int(i // j)
            i %= j
        array.append(cnt)
    print(*array)