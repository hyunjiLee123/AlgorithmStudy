n = int(input())
food = input().split()
my_food = input().split()

for f in food:
    if f not in my_food:
        print(f)