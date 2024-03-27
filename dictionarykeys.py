Using items() method: You can iterate over key-value pairs of the dictionary using the items() method.
python
Copy code
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(key, value)
  
Using keys() method: You can iterate over keys and then access values using the keys.
python
Copy code
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict.keys():
    print(key, my_dict[key])
  
Using values() method: You can iterate over values directly.
python
Copy code
my_dict = {'a': 1, 'b': 2, 'c': 3}
for value in my_dict.values():
    print(value)

Using comprehension: You can use dictionary comprehensions to iterate over key-value pairs.
python
Copy code
my_dict = {'a': 1, 'b': 2, 'c': 3}
parsed_data = {key: value for key, value in my_dict.items()}

Using get() method: You can use the get() method to access values by key.
python
Copy code
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.get('a'))  # Output: 1
