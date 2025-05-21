import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mon = {}
num = {}

for n in range(1, N+1):
    nn = input().strip()
    mon[n] = nn
    num[nn] = n

for m in range(M):
    mm = input().strip()
    if mm.isnumeric():
        print(mon[int(mm)])
    else:
        print(num[mm])
