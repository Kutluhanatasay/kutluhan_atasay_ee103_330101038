# calc_factorial_while.py
# EE103 Week 3 - Part 5: Factorial using a WHILE loop

num = int(input("Enter a number to calculate its factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    current = num
    while current > 1:
        factorial *= current
        current -= 1
    print(f"Factorial of {num} is: {factorial}")
