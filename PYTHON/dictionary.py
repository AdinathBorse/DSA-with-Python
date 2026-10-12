empName = input("Name :")
empid = int(input("id :"))
empSal = int(input("Salary :"))
emp = {
    "Name":empName,
    "ID":empid,
    "Salary":empSal
    }


print(emp)

# 1. Definition
# A dictionary stores related values as key-value pairs, so each value can be
# looked up by a descriptive key.
#
# 2. Explanation
# This program reads an employee name and converts the ID and salary inputs to
# integers. It then stores the three values under the keys Name, ID, and Salary.
# Dictionaries are useful for representing one record with named fields.
#
# 3. Real-life example
# An employee record can label a person's details as name, ID number, and salary
# instead of relying on their position in a list.
#
# 4. Example (with code)
# name = input("Name :")
# employee_id = int(input("id :"))
# salary = int(input("Salary :"))
# employee = {"Name": name, "ID": employee_id, "Salary": salary}
# print(employee)
#
# 5. Output Explanation
# If the inputs are Ada, 101, and 75000, the output is:
# {'Name': 'Ada', 'ID': 101, 'Salary': 75000}
# Each key is paired with its entered value. The ID and salary appear as
# integers because int() converts those inputs from text.
#
# 6. Summary
# - Dictionaries store key-value pairs.
# - Keys label the meaning of their values.
# - input() returns text; int() converts numeric text to an integer.
# - Use a dictionary to keep related, named data together.
