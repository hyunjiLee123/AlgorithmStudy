import sys

N = int(input())
N_list = sys.stdin.readline().split()
N_set = set(N_list)
M = int(input())
M_list = sys.stdin.readline().split()

for m in M_list:
    print(1 if m in N_set else 0)