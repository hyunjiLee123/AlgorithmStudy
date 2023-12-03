n = int(input())
while n != -1:
    factor = []
    for i in range(1, n+1):
        if n % i == 0:
            factor.append(i)
    sum = 0
    for f in range(len(factor)-1):
        sum += factor[f]

    if sum == factor[len(factor)-1]:
        print(sum, "= ", end='')
        for ff in range(len(factor)-2):
            print(factor[ff], '+ ', end='')
        print(factor[len(factor)-2])

    else:
        print(factor[len(factor)-1], "is NOT perfect.")

    n = int(input())