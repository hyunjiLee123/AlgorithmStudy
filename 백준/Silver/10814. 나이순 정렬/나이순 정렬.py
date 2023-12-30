num = []
N = int(input())
for n in range(N):
    ab = list(map(str, input().split()))
    num.append(ab)

for ll in num:
    ll[0] = int(ll[0])

num = sorted(num, key=lambda x:x[0])

for i in range(N):
    print(num[i][0], num[i][1])