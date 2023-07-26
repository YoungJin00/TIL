# 약수들의 합

li = []
while 1:
    a = int(input())
    if a == -1:
        break

    for i in range(1, a+1):
        if a % i == 0:
            li.append(i)
    if sum(li) == a:
        print(a, " = ", " + ".join(str(i) for i in li), sep="")
    else:
        print(a, "is NOT perfect.")



