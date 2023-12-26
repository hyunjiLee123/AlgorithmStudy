num = []
N = int(input())
for n in range(N):
    ab = list(map(int, input().split()))
    num.append(ab)

num.sort()
for i in range(N):
    print(num[i][0], num[i][1])