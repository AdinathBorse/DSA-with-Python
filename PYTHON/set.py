emp = set()

for i in range(1,5):
    
    emp.add(input("EmpName :"))
    
print(emp)

# 1. Definition
# A set is a collection of distinct values. It does not keep duplicate values,
# and its display order is not guaranteed.
#
# 2. Explanation
# This program creates an empty set and asks for four employee names. add() puts
# each name into the set. If the same name is entered more than once, the set
# stores it only once. Sets are useful for membership checks and unique values.
#
# 3. Real-life example
# A guest list can be treated as a set when each person's name should appear
# only once, even if someone is added more than once.
#
# 4. Example (with code)
# employees = set()
# for i in range(1, 5):
#     employees.add(input("EmpName :"))
# print(employees)
#
# 5. Output Explanation
# If the entries are Ana, Bo, Ana, and Cam, the set contains Ana, Bo, and Cam.
# The printed set has those three unique names, but their order may vary, for
# example: {'Ana', 'Bo', 'Cam'}.
#
# 6. Summary
# - Sets keep unique values and discard duplicates.
# - add() inserts a value into a set.
# - A set is not intended for positional indexing.
# - The order shown when printing a set may vary.