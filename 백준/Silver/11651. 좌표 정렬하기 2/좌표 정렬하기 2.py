num = []
N = int(input())
for n in range(N):
    ab = list(map(int, input().split()))
    num.append(ab)

for ll in num:
    temp = ll[0]
    ll[0] = ll[1]
    ll[1] = temp

num.sort()

for i in range(N):
    print(num[i][1], num[i][0])