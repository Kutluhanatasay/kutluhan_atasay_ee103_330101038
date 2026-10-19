# week03 Task 5.1

n = int(input("enter integer number to calculate its factorial"))
k = int(1)

if n == 0:
    print("1")
else:
    for i in range(1, n):
        n = n * i

    print(n)
    


