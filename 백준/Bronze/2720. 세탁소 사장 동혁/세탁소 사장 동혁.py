T = int(input())
for i in range(T):
    C = int(input())
    a25 = C // 25
    a10 = (C%25) // 10
    a5 = ((C % 25) % 10) // 5
    aa = ((C % 25) % 10) % 5

    print(a25, a10, a5, aa)