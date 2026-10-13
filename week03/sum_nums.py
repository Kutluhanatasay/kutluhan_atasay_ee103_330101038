# sum_nums.py
# EE103 Week 3 - Part 6: Running Sum & Gauss Summation Verification

num = int(input("Enter a number: "))

# Calculate running sum using a loop
total_sum = 0
for i in range(1, num + 1):
    total_sum += i

print(f"Sum calculated by loop: {total_sum}")

# Calculate sum directly using Gauss summation law
sum_gauss = num * (num + 1) / 2
print(f"Sum calculated by Gauss law: {sum_gauss}")

# Check if both results are equal
if total_sum == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")
