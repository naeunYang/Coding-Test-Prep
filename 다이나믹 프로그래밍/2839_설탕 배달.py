import sys

n = int(sys.stdin.readline()) # kg
array = [3, 5] # 설탕 봉지 종류

# dp 테이블 초기화, 1kg ~ nkg 최소 봉지 갯수 저장
d = [5001] * (n + 1)
d[0] = 0

for j in array:
    for i in range(1, n + 1):
        if d[i - j] != 5001:
            d[i] = min(d[i], d[i - j] + 1)

if d[n] == 5001:
    print(-1)
else:
    print(d[n])

# => 메모리: 32412KB, 시간: 40ms, 코드 길이: 352B