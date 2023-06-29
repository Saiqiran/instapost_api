set = {1, 2, 3}  # Using curly braces
set = set([1, 2, 3])  # Using the set() function

set.add(4)  # Adding a single element to the set
set.update([5, 6, 7])  # Adding multiple elements to the set

set.remove(3)  # Removing a specific element from the set
set.discard(4)  # Removing an element if it exists, without raising an error

set.pop()  # Removing and returning an arbitrary element from the set
set.clear()  # Removing all elements from the set, making it empty

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # Output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)  # Output: {3}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)  # Output: {1, 2}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)  # Output: {1, 2, 4, 5}

3 in set  # Checking if an element is present in the set

len(set)  # Getting the number of elements in the set

for element in set:
    print(element)

## looping ###


##  for loop ###
set = {1, 2, 3, 4, 5}
for element in set:
    print(element)

##  sorted  ##
set = {5, 1, 3, 4, 2}
for element in sorted(set):
    print(element)


##  compact loop ##         *******
set = {1, 2, 3, 4, 5}
[print(element) for element in set]


## while ###
set = {1, 2, 3, 4, 5}
temp_set = set.copy()
while temp_set:
    element = temp_set.pop()
    print(element)
