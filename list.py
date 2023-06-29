list = [1,2,3,4,5]

list.insert(1, 99) # to in insert a number in a plsce

print(list[0:6]) # to get the betweeen numbers

list[0] = 10  # Changing the value at index 0 to 10

list.remove(3)  # Removing the first occurrence of the value 3
ele = list.pop()  # Removing the last element from the list  (LAST DIGIT IS REMOVING BECAUSE IT IS FOLLOWING QUE OPERATIONS)

list.reverse()  # Reversing the order of elements in the list

list.sort()  # Sorting the list in ascending order
list.sort(reverse=True)  # Sorting the list in descending order

3 in my_list  # Checking if 3 is present in the list

print(list[1:4])  # Extracting a sublist from index 1 to 3 (excluding 4)
print(list[:3])  # Extracting a sublist from the beginning to index 2 (excluding 3)
print(list[3:])  # Extracting a sublist from index 3 to the end

list.append(6)  # Adding an element at the end of the list
list.extend([7, 8, 9])  # Adding multiple elements to the end of the list

print(list[0])  # Output: 1 (accessing the first element)
print(list[-1])  # Output: 5 (accessing the last element)


#####  LOOPING   ###

##  FOR LOOP ##
list = [1, 2, 3, 4, 5]
for element in list:
    print(element)


##   RANGE  ##
list = [1, 2, 3, 4, 5]

for i in range(len(list)):
    print(list[i])

####  enumerate  ##

list = [1, 2, 3, 4, 5]
for index, element in enumerate(list):
    print(f"Index: {index}, Element: {element}")

### while looop  ##

list = [1, 2, 3, 4, 5]
i = 0
while i < len(list):
    print(list[i])
    i += 1


