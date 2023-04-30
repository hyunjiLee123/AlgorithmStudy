ch_list = []
grade_list = []
answer = []
summ = 0
gradee = 0

for i in range(20):
    name, p, grade = map(str, input().split())
    ch_list.append([p, grade])

for l in ch_list:
    if l[1] == 'A+':
        grade_list.append([l[0], '4.5'])
    elif l[1] == 'A0':
        grade_list.append([l[0], '4.0'])
    elif l[1] == 'B+':
        grade_list.append([l[0], '3.5'])
    elif l[1] == 'B0':
        grade_list.append([l[0], '3.0'])
    elif l[1] == 'C+':
        grade_list.append([l[0], '2.5'])
    elif l[1] == 'C0':
        grade_list.append([l[0], '2.0'])
    elif l[1] == 'D+':
        grade_list.append([l[0], '1.5'])
    elif l[1] == 'D0':
        grade_list.append([l[0], '1.0'])
    elif l[1] == 'F':
        grade_list.append([l[0], '0.0'])
    elif l[1] =='P':
        continue

if len(grade_list) == 0:
    summ = 0
    gradee = 0
else:
    for l in grade_list:
        summ += float(l[0]) * float(l[1])
        gradee += float(l[0])

print(f'{summ/gradee:.6f}'.format(summ / gradee))