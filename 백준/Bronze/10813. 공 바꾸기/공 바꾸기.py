answer = []
ij = []

N, M = map(int, input().strip().split())
for m in range(M):
    i, j = map(int, input().strip().split())
    ij.append([i, j])

for i in range(N):
    answer.append(i+1)

for l in ij:
    i = l[0]
    j = l[1]
    swap = answer[i-1]
    answer[i-1] = answer[j-1]
    answer[j-1] = swap

for a in answer:
    print(a, end=" ")