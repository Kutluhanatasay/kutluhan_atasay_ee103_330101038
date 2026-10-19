# week03 Task 5.2

n = int(input("enter integer number to calculate its factorial"))
i = int(1)
F = int(n)
if n == 0:
    print("1")
else:
    while n > 1:
        F = F * (n - 1)
        n = (n - 1)

    print(F) 


