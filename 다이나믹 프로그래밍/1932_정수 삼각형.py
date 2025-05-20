import sys

n = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = array

for i in range(1, n):
    for j in range(i + 1):
        # 조건: 왼쪽 위에서 오는 경우, 오른쪽 위에서 오는 경우
        
        # 왼쪽 위에서 오는 경우
        if j == 0: # 첫번째 열은 왼쪽 위가 없으므로 0 처리
            left_up = 0
        else:
            left_up = dp[i - 1][j - 1]

        # 오른쪽 위에서 오는 경우
        if j == i: # 맨 끝 열은 오른쪽 위가 없으므로 0 처리
            right_up = 0
        else:
            right_up = dp[i - 1][j]
        
        dp[i][j] = dp[i][j] + max(left_up, right_up)

print(max(dp[n - 1]))

# => 메모리: 36504KB, 시간: 116ms, 코드 길이: 741B