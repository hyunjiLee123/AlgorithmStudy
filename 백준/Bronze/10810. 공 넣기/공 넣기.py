answer = []
ijk = []

N, M = map(int, input().strip().split())
for m in range(M):
    i, j, k = map(int, input().strip().split())
    ijk.append([i, j, k])

for i in range(N):
    answer.append(0)

for l in ijk:
    i = l[0]
    j = l[1]
    k = l[2]
    while (j-i >= 0):
        answer[i-1] = k
        i += 1

for a in answer:
    print(a, end=" ")