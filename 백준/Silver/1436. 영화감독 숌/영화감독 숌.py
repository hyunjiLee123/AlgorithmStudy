N = int(input())
num = 666
count = 0
answer = True

while answer:
    if '666' in str(num):
        count += 1
    if count == N:
        print(num)
        answer = False

    num += 1