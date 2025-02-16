import sys
import re	#정규표현식을 위한 모듈

#빠른 입력
fast_input = sys.stdin.readline().strip()

#입력
cnt = int(fast_input)	#입력 값 수
sirals = [input() for _ in range(cnt)]	#배열 입력

#정렬
sirals.sort( key = lambda x : ((len(x)), addNum(x), x ))

#출력
for s in sirals:
	print(s)


#1조건 함수 : 문자열 내의 숫자 합산
def addNum (sNO):
	result = 0
	# 문자에 숫자가 있을 경우 합산
	for x in re.findall(r"\d", sNO):
		result += int(x)
	
	return result