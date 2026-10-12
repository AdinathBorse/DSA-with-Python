a = []
n = int(input("Enter the number of Element in list :"))
for i in range (n) :
    num = int(input("Enter the number:"))
    a.append(num)

# 1. Definition
# This program demonstrates collecting integer values in a list. It does not
# currently test whether the values are odd or even.
#
# 2. Explanation
# The program asks how many numbers to collect, repeats the input prompt that
# many times, converts each entry to an integer, and appends it to the list.
# It has no print statement, so it does not display the list or classify values.
# Lists are useful for storing a sequence of values to process later.
#
# 3. Real-life example
# This is like writing a set number of daily temperatures into a notebook before
# later calculating an average or sorting them.
#
# 4. Example (with code)
# numbers = []
# count = int(input("Enter the number of Element in list :"))
# for i in range(count):
#     number = int(input("Enter the number:"))
#     numbers.append(number)
#
# 5. Output Explanation
# If the count is 3 and the entries are 2, 5, and 8, the program displays the
# input prompts, but no final list or odd/even result. The values are collected
# in the list while the program runs.
#
# 6. Summary
# - The program collects a user-selected number of integers.
# - int() converts each numeric entry from text to an integer.
# - append() adds each integer to the end of the list.
# - Despite the filename, no odd/even check is currently performed.
    
