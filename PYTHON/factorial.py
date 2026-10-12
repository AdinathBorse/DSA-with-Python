fact =1
num = int(input("Enter the numbers :"))
for i in range (num):
    fact *= num-i
print(fact)    

# 1. Definition
# A factorial is the product of all positive integers from 1 up to a number n,
# written n!. By definition, 0! is 1.
#
# 2. Explanation
# The variable fact starts at 1, the neutral value for multiplication. The loop
# multiplies it by num, then num - 1, continuing down to 1. For a non-negative
# integer n, this calculates n!. Factorials are used in counting and combinatorics.
#
# 3. Real-life example
# If five different books are arranged in a row, there are 5! possible orders:
# five choices for the first position, then four, and so on.
#
# 4. Example (with code)
# fact = 1
# num = int(input("Enter the numbers :"))
# for i in range(num):
#     fact *= num - i
# print(fact)
#
# 5. Output Explanation
# For input 5, the calculation is 5 * 4 * 3 * 2 * 1, so the output is:
# 120
# For input 0, the loop runs zero times and fact remains 1, giving 0! = 1.
#
# 6. Summary
# - Factorial multiplies all positive integers up to the input.
# - The loop counts down through the factors.
# - Starting at 1 makes the multiplication work, including for zero.
# - This program is intended for non-negative integer inputs.