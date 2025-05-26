import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_dict = {}
for n in N_list:
    if n in N_dict:
        N_dict[n] += 1
    else:
        N_dict[n] = 1

answer = []
for m in M_list:
    if m in N_dict:
        answer.append(N_dict[m])
    else:
        answer.append(0)

print(' '.join(map(str, answer)))