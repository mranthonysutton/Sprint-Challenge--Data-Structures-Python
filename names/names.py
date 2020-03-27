import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# creates a new BinarySearchTree
search_tree = BinarySearchTree("name")

# Loops through all the names in names_1 and inserts them into a list
for name in names_1:
	search_tree.insert(name)

# Loops through all the names in names_2 and if it contains the name, andds to the duplicate array
for name in names_2:
	if search_tree.contains(name):
		duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
stretch_start_time = time.time()

dict_names = {}
duplicate_result = []

for name in names_1:
	dict_names[name] = 1

for name in names_2:
	if name in dict_names:
		duplicate_result.append(name)

stretch_end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"STRETCH RUNTIME: {stretch_end_time - stretch_start_time} seconds")