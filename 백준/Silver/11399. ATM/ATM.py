def solution():
    answer = 0
 
    for i in range(N):
        for j in range(0, i+1):
            answer += arr[j]
 
    return answer
 
 
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(solution())