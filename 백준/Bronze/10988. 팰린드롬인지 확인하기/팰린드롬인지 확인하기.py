name = input()
name2=""
for i in range(len(name)-1,-1,-1):
    name2+=name[i]  # for문으로 문자를 역순으로 name2에 저장
if name==name2:
    print(1)
else:
    print(0)