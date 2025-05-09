# teamCnt = list(map(int, input().split()))
# damageTeams = list(map(int, input().split()))
# spareTeams = list(map(int, input().split()))

# result = 0
# for team in damageTeams:
#     if team - 1 in spareTeams: 
#         spareTeams.remove(team - 1)
#     elif team + 1 in spareTeams:
#         spareTeams.remove(team + 1)
#     elif team in spareTeams:
#         spareTeams.remove(team)
#     else:
#         result += 1

# print(result)


import sys

# input() 대신 표준 입력, 리스트 컴프리헨션 사용하여 입력을 받음
# 차집합을 사용하기 위해서 list 대신 set을 사용함
team_cnt, damage_teams, spare_teams = [set(map(int, sys.stdin.readline().split())) for _ in range(3)]
absent_team_cnt = 0

# 손상된 카약이자 여분을 갖고 있는 팀일 경우, 여분 카약을 빌려주지 못함
# -> damage_teams와 spare_teams에서 해당 팀 제외시켜야 함
intersection_team = damage_teams & spare_teams # 손상팀이자 여분을 갖고 있는 팀 추출
damage_teams -= intersection_team # 손상팀에서 제외
spare_teams -= intersection_team # 여분팀에서 제외

for team in damage_teams:
    if team - 1 in spare_teams:
        spare_teams.remove(team - 1)
    elif team + 1 in spare_teams:
        spare_teams.remove(team + 1)
    else:
        absent_team_cnt += 1

print(absent_team_cnt)