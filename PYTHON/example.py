a = []
n = int(input("Enter the number of Element in list :"))
for i in range (n) :
    sub = input("Enter the subject :")
    a.append(sub)
print(a)

# 1. Definition
# This program demonstrates building a list from user input with a loop.
#
# 2. Explanation
# The user first enters how many subjects to collect. range(n) repeats the loop
# n times. Each subject is appended to the list, and the completed list is
# printed. A list is useful when the number of items may vary.
#
# 3. Real-life example
# A student could enter the subjects they are taking this term, one at a time,
# and keep them together as a list.
#
# 4. Example (with code)
# subjects = []
# count = int(input("Enter the number of Element in list :"))
# for i in range(count):
#     subject = input("Enter the subject :")
#     subjects.append(subject)
# print(subjects)
#
# 5. Output Explanation
# If the count is 3 and the subjects are Math, Science, and English, the output is:
# ['Math', 'Science', 'English']
# The loop adds one subject per repetition; print() displays the final list.
#
# 6. Summary
# - A list can grow as items are appended.
# - range(count) repeats a loop count times.
# - input() reads each subject as text.
# - The printed list contains the entered subjects in order.

