a = [10,20,30,40]
b = [40,50,60,70]
for i in b :
     a.append(i)
    
print(a) 

# 1. Definition
# This program combines two lists by appending every item from the second list
# to the first list.
#
# 2. Explanation
# The for loop visits each value in b and append() adds it to a. The original
# items in a stay first, followed by the items from b. Duplicates are preserved;
# this is list concatenation by repeated appending, not set union.
#
# 3. Real-life example
# Two queues of tasks can be combined by placing every task from the second queue
# after all tasks already in the first queue.
#
# 4. Example (with code)
# first = [10, 20, 30, 40]
# second = [40, 50, 60, 70]
# for item in second:
#     first.append(item)
# print(first)
#
# 5. Output Explanation
# The output is:
# [10, 20, 30, 40, 40, 50, 60, 70]
# The original 40 from each list is retained, so 40 appears twice.
#
# 6. Summary
# - A list preserves item order.
# - append() adds one item to the end of a list.
# - Looping over the second list adds all of its items.
# - Repeated values are not removed.
