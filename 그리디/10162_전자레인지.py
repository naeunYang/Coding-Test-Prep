import sys

T = int(sys.stdin.readline())
buttons = [300, 60, 10]

cnt = [0, 0, 0]
for i in range(len(buttons)):
    if T >= buttons[i]:
        cnt[i] = (T // buttons[i])
        T %= buttons[i]
        
if T > 0:
    print(-1)
else:
    print(*cnt)