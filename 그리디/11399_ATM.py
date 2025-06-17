import sys

n = int(sys.stdin.readline())
p = sorted(list(map(int, sys.stdin.readline().split())))

result = 0

for i in range(len(p)):
    cnt = 0
    for k in range(i + 1):
        cnt += p[k]
    result += cnt

print(result)

# => 메모리: 32412KB, 시간: 108ms, 코드 길이: 227B