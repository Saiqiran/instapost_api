tuple = (1, 2, 3, 4, 5)

print(tuple[0])  # Output: 1 (accessing the first element)
print(tuple[-1])  # Output: 5 (accessing the last element)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2  # Output: (1, 2, 3, 4, 5, 6)

tuple[1:4]  # Extracting a subtuple from index 1 to 3 (excluding 4)
tuple[:3]  # Extracting a subtuple from the beginning to index 2 (excluding 3)
tuple[3:]  # Extracting a subtuple from index 3 to the end

3 in tuple  # Checking if 3 is present in the tuple

len(tuple)  # Getting the number of elements in the tuple

nested_tuple = ((1, 2), (3, 4), (5, 6))  # Tuples can be nested within each other  ********

a, b, c = tuple  # Unpacking tuple elements into separate variables

for element in tuple:
    print(element)

tuple.count(3)  # Counting the number of occurrences of the value 3

tuple.index(4)  # Finding the index of the value 4 in the tuple


####    looping    #####

## for ##
tuple = (1, 2, 3, 4, 5)
for element in tuple:
    print(element)

## range ##
tuple = (1, 2, 3, 4, 5)
for i in range(len(tuple)):
    print(tuple[i])

##  enumerate  ##
tuple = (1, 2, 3, 4, 5)
for index, element in enumerate(tuple):
    print(f"Index: {index}, Element: {element}")

## while ##
tuple = (1, 2, 3, 4, 5)
i = 0
while i < len(tuple):
    print(tuple[i])
    i += 1



