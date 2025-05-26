import sys

n = int(sys.stdin.readline())

d = [0] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[n])

# 일반적인 기준
# 시간제한   허용 연산 수     권장 알고리즘
#   1초       1억(10^8)      O(N log N) 이하
#  0.5초    5천만(5*10^7)    O(N log N) 이하
#  0.15초  약 1천만(1*10^7)  O(N) or 매우 빠른 O(N log N)

# => 메모리: 40224KB, 시간: 468ms, 코드 길이: 244B