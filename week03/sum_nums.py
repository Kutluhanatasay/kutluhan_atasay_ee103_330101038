# week 03 task 6

sum = int()
n = int(input("enter a integer to find its sum 1-n"))
i = int(n)
sum_gauss = int()

while n > 0:
    sum = sum + n
    n = n - 1

print(sum)

sum_gauss = i * (i + 1) / 2
print(sum_gauss)

if sum == sum_gauss :
    print("program works succsesfully")
else:
    print("program is not working ")