import sys

input = sys.stdin.readline

N = int(input())
N_list = set(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

answer = []

for num in M_list:
    if num in N_list:
        answer.append('1')
    else:
        answer.append('0')

print(' '.join(answer))
