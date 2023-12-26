N, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
print(num[N-k])