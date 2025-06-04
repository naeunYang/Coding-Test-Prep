import sys

n = int(sys.stdin.readline())
glasses = [int(sys.stdin.readline()) for _ in range(n)]

if n == 1:
    print(glasses[0])
elif n == 2:
    print(glasses[0] + glasses[1])
else:
    # i번째 포도주까지의 최적의 해
    # 1. 이번 잔을 마시지 않는다. d[i] = d[i - 1]
    # 2. 이번 잔을 마시고, 바로 이전 잔은 마시지 않는다. d[i] = d[i - 2] + glasses[i]
    # 3. 이번 잔과 바로 이전 잔을 마시고, 그 전 잔은 마시지 않는다. d[i] = d[i - 3] + glasses[i - 1] + glasses[i]
    d = [0] * n

    d[0] = glasses[0]
    d[1] = glasses[0] + glasses[1]
    d[2] = max(d[1], glasses[2] + glasses[0], glasses[2] + glasses[1])
    for i in range(3, n):
        d[i] = max(d[i - 1], d[i - 2] + glasses[i], d[i - 3] + glasses[i - 1] + glasses[i])

    print(d[n - 1])

# => 메모리: 33432KB, 시간: 40ms