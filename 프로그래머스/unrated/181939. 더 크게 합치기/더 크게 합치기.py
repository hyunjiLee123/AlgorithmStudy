def solution(a, b):
    answer = 0
    
    ans1 = str(a) + str(b)
    ans2 = str(b) + str(a)

    if int(ans1) > int(ans2):
        answer = int(ans1)
    else:
        answer = int(ans2)
    
    return answer