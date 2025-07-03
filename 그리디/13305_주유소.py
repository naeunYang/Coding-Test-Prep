import sys

n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

min_price = price[0]
result = 0

# 현재까지의 최소 기름 가격을 저장
for i in range(len(price) - 1):
    min_price = min(min_price, price[i])
    result += min_price * distance[i]

print(result)