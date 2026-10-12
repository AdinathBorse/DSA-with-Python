num = int(input("Enter the number : "))

for i in range (1,11):
    print(num,"*",i,"=",num*i)

# 1. Definition
# A multiplication table lists the products of a chosen number and a sequence
# of multipliers.
#
# 2. Explanation
# The program reads one integer, then range(1, 11) supplies the multipliers 1
# through 10. Each loop iteration calculates and prints one product. Tables are
# useful for practicing multiplication and viewing repeated multiples.
#
# 3. Real-life example
# If one ticket costs 7 dollars, the table for 7 shows the total cost of buying
# between one and ten tickets.
#
# 4. Example (with code)
# number = int(input("Enter the number : "))
# for multiplier in range(1, 11):
#     print(number, "*", multiplier, "=", number * multiplier)
#
# 5. Output Explanation
# For input 7, the first and last lines are:
# 7 * 1 = 7
# 7 * 10 = 70
# There are ten lines total; each iteration increases the multiplier by 1.
#
# 6. Summary
# - The chosen number is multiplied by each value from 1 through 10.
# - range(1, 11) excludes 11, so the last multiplier is 10.
# - The loop prints one multiplication fact per iteration.
# - Changing the range changes how many rows are displayed.
    
    