N = int(input())
time = list(map(int,input().split()))
time.sort(reverse=True)
grow = []
result = []

for i in range(N):
    grow.append(i+2)

for j in range(N):
    result.append(time[j]+grow[j])

print(max(result))