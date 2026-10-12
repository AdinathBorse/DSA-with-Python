number = input("enter the number :")
sum = 0
for i in number:
    sum += int(i)
print("The sum of digit is :",sum)

# 1. Definition
# This program calculates the sum of the digits in a number by adding each
# digit's numeric value.
#
# 2. Explanation
# input() reads the number as text, so the for loop can visit its characters one
# at a time. int(i) converts each digit character to an integer, and the running
# total is updated on every iteration. This approach is useful for processing
# the individual digits of a non-negative whole number.
#
# 3. Real-life example
# A person might add the digits on a raffle ticket to get a small check value,
# such as 1 + 2 + 3 + 4 for ticket 1234.
#
# 4. Example (with code)
# number_text = input("enter the number :")
# total = 0
# for digit in number_text:
#     total += int(digit)
# print("The sum of digit is :", total)
#
# 5. Output Explanation
# For input 1234, the output is:
# The sum of digit is : 10
# The loop adds 1, then 2, then 3, then 4, producing a total of 10.
#
# 6. Summary
# - input() provides text that can be processed character by character.
# - int() converts each digit character to a number.
# - The total accumulates the digit values.
# - This version expects digits only; a negative sign is not a digit.