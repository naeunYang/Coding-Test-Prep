import sys
input = sys.stdin.readline   #빠른입력

#입력데이터
#입력 받기 + 행별 분할 (cnt데이터, 부서진 팀들, 여분팀들)
#탐색의 시간 복잡도를 줄이기 위해 set 사용
data, brokenTeams, subTeams = [set(map(int, input().split(" "))) for i in range(3)]

#list를 변수로 해체 및 할당 (전체팀수, 부서진팀수, 여분팀수)
# all, brokenCnt, subCnt = [data[i] for i in range(3)]

#교집합 연산
left = brokenTeams - subTeams # 출전 불가 팀들
sub = subTeams - brokenTeams # 여분 있는 팀들

# 깊은 복사
remainTeams = left.copy()

for team in sub:
	if team - 1 in left and team - 1 in remainTeams:	#앞팀
		remainTeams.remove(team-1)
	elif team + 1 in left and team + 1 in remainTeams:	#뒷팀
		remainTeams.remove(team+1)

	#부서진팀의 수가 0이 될 경우 종료
	if len(remainTeams) == 0:
		break

print(len(remainTeams))