a = input()
b = input()
c = input()
ans_s1 = ''
ans_s2 = ''
ans_i = 0

colors = [['black', '0', 1], ['brown', '1', 10], ['red', '2', 100], ['orange', '3', 1000], ['yellow', '4', 10000],
          ['green', '5', 100000], ['blue', '6', 1000000], ['violet', '7', 10000000], ['grey', '8', 100000000], ['white', '9', 1000000000]]

for cc in colors:
    if a == cc[0]:
        ans_s1 += cc[1]
    if b == cc[0]:
        ans_s2 += cc[1]
    if c == cc[0]:
        ans_i = cc[2]

print(int(ans_s1 + ans_s2)*ans_i)