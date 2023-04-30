n, m = map(int, input().strip().split())
bem = []
answer = []
for i in range(m):
    b, e, m = map(int, input().strip().split())
    bem.append([b, e, m])

for i in range(1, n+1):
    answer.append(i)

for l in bem:
    begin = l[0]
    end = l[1]
    mid = l[2]
    swap = answer[mid-1:end]
    answer[mid-1:end] = answer[begin-1:mid-1]
    answer[begin-1:mid-1] = swap

for i in answer:
    print(i, end=' ')
