def solution(array):
    answer = 0
    i = int(len(array) / 2)
    arr = sorted(array)
    answer = arr[i]
    return answer