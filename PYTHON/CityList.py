
cities = []
for i in range (1,6):
    cities.append(input("City Names :"))
    
uc = input("updated list :")
cities[2] = uc
cities = cities[0:4]
print(cities)

# 1. Definition
# This program demonstrates list operations: appending items, replacing an
# item by its index, and selecting a range of items with a slice.
#
# 2. Explanation
# The loop collects five city names and appends each one to the list. Python
# indexes start at 0, so cities[2] refers to the third city. That item is
# replaced with the new city name. The slice cities[0:4] keeps indexes 0 to 3;
# the ending index 4 is excluded, so the fifth city is removed.
#
# 3. Real-life example
# Think of a five-stop travel itinerary: replace its third stop, then keep only
# the first four stops.
#
# 4. Example (with code)
# cities = []
# for i in range(1, 6):
#     cities.append(input("City Names :"))
# updated_city = input("updated list :")
# cities[2] = updated_city
# cities = cities[0:4]
# print(cities)
#
# 5. Output Explanation
# Sample input: Paris, Tokyo, Delhi, Cairo, Lima, then Seoul as the replacement.
# Expected output: ['Paris', 'Tokyo', 'Seoul', 'Cairo']
# Seoul replaces Delhi at index 2, and the slice excludes Lima at index 4.
#
# 6. Summary
# - Lists keep items in order.
# - Index 2 means the third item because indexing starts at 0.
# - Assignment at an index replaces that item.
# - A slice excludes its ending index.

