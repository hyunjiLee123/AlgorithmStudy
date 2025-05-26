A, B = map(int, input().split())
A_list = set(map(int, input().split()))
B_list = set(map(int, input().split()))

cnt = 0
for a in A_list:
    if a in B_list:
        cnt += 1

print(A+B-2*cnt)