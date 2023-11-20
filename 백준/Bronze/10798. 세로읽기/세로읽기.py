word_list = []
len_list = []
answer = []
for i in range(5):
    x = input()
    word_list.append(x)
    len_list.append(len(x))


for m in range(max(len_list)):
    for w in word_list:
        if len(w) <= m:
            continue
        else:
          answer.append(w[m])

for a in answer:
    print(a, end='')
