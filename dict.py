dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}  # Using curly braces
dict = dict(key1='value1', key2='value2', key3='value3')  # Using the dict() function

value = dict['key1']  # Accessing the value associated with 'key1'

dict['key2'] = 'new_value'  # Modifying the value associated with 'key2'

dict['key4'] = 'value4'  # Adding a new key-value pair to the dictionary

del dict['key3']  # Removing a specific key-value pair from the dictionary
dict.pop('key2')  # Removing and returning the value associated with 'key2'
dict.popitem()  # Removing and returning an arbitrary key-value pair
dict.clear()  # Removing all key-value pairs from the dictionary, making it empty

'key1' in dict  # Checking if a key exists in the dictionary

len(dict)  # Getting the number of key-value pairs in the dictionary

keys = dict.keys()  # Returning a list of all keys in the dictionary
values = dict.values()  # Returning a list of all values in the dictionary

for key in dict:
    print(key)  # Iterating over keys

for value in dict.values():
    print(value)  # Iterating over values

for key, value in dict.items():
    print(f"Key: {key}, Value: {value}")  # Iterating over key-value pairs

