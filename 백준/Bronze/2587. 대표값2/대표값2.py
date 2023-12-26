num = []
for i in range(5):
    N = int(input())
    num.append(N)

num.sort()
s = 0
for j in range(5):
    s += num[j]

print(int(s/5))
print(num[2])