import sys

n, m = list(map(int, sys.stdin.readline().split())) # n: 나무 수, m: 나무 길이
array = list(map(int, sys.stdin.readline().split())) # 나무 높이

start = 0 # 시작점
end = max(array) # 끝점

result = 0

# 이진 탐색 수행
while start <= end:
    mid = (start + end) // 2 # 중간점
    total = 0 # 길이 합을 저장

    for i in array:
        if i >= mid:
            total += i - mid

    # 길이가 부족한 경우(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 길이가 충분한 경우(오른쪽 부분 탐색)
    else:
        result = mid
        start = mid + 1
        

print(result)

# 이진 탐색의 시간 복잡도는 O(logN)을 보장한다.