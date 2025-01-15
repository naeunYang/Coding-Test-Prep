# 정렬 
# import sys

# n = int(input())
# serials = [sys.stdin.readline().rstrip() for _ in range(n)]

# # 숫자의 합을 계산하는 함수
# def digit_sum(string):
#     return sum(int(char) for char in string if char.isdigit()) # 숫자인 문자열이면 sum

# # 삽입 정렬로 구현한 코드
# for i in range(1, len(serials)):
#     for j in range(i, 0, -1):
#         if len(serials[j]) < len(serials[j - 1]): # 1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
#             serials[j], serials[j - 1] = serials[j - 1], serials[j]
#         elif len(serials[j]) == len(serials[j - 1]): 
#             # 2. 길이가 같다면, 작은 합을 가지는 것이 먼저 온다.
#             if digit_sum(serials[j]) < digit_sum(serials[j - 1]):
#                 serials[j], serials[j - 1] = serials[j - 1], serials[j]
#             # 3. 1, 2조건으로 비교할 수 없다면, 사전 순으로 비교한다.(길이가 같고, 합계도 같은 경우)
#             elif digit_sum(serials[j]) == digit_sum(serials[j - 1]) and serials[j] < serials[j - 1]:
#                 serials[j], serials[j - 1] = serials[j - 1], serials[j]
#         else: 
#             break

# for serial in serials:
#     print(serial)

# => 최악의 경우 O(N^2)의 시간 복잡도를 가진다.
# => 메모리: 32412KB, 시간: 76ms, 코드 길이: 1152B



import sys

n = int(input())
serials = [sys.stdin.readline().rstrip() for _ in range(n)]

# 숫자의 합을 계산하는 함수
def digit_sum(string):
    return sum(int(char) for char in string if char.isdigit()) # 숫자인 문자열이면 sum

serials.sort(key=lambda x: (len(x), digit_sum(x), x))
# sort()의 key속성을 이용한 다중 정렬
# -> key는 각 매개변수에 대해 정렬 기준을 튜플로 반환한다.
# -> len(x): 문자열의 길이, digit_sum(x): 문자열에 포함된 숫자의 값, x: 문자열 자체(사전)

for serial in serials:
    print(serial)

# => 내장된 sort()를 사용하면 최악의 경우에도 O(NlogN)의 복잡도를 보장한다.
# => 메모리: 32412KB, 시간: 40ms, 코드 길이: 557B