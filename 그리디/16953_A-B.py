import sys

a, b = list(map(int, sys.stdin.readline().split()))

cnt = 1
while a < b:
    # 짝수일 경우
    if b % 2 == 0:
        b //= 2
    # 1로 끝날 경우
    elif b % 10 == 1:
        b //= 10
    else:
        cnt = -1
        break
    
    cnt += 1

if a == b:
    print(cnt)
else:
    print(-1)