import sys

n = int(sys.stdin.readline())
meetings = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(n) ]
sorted_mettings = sorted(meetings, key=lambda x: (x[1], x[0])) # 끝나는 시간이 같을 때는 시작 시간이 빠른 회의가 먼저 오도록 설정

cnt = 0
end_time = 0

# 끝나는 시간이 빠르면 더 많은 회의를 넣을 수 있는 가능성이 크다.
for i in sorted_mettings:
    if(end_time <= i[0]):
        cnt += 1
        end_time = i[1]

print(cnt)