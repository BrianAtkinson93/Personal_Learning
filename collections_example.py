from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Using Counter to count the occurrences of elements in a list
print("=== Counter ===")
fruits = ['apple', 'banana', 'orange', 'apple', 'banana', 'grape', "banana"]
fruit_count = Counter(fruits)
print(fruit_count)
print(fruit_count.most_common()[0])

# Using namedtuple to create a simple class to store data
print("\n=== namedtuple ===")
Person = namedtuple('Person', ['name', 'age', 'gender'])
person1 = Person(name='John', age=30, gender='Male')
print(person1)
print(f'persons name: {person1.name}')
print(f"persons age: {person1.age}")

# Using OrderedDict to maintain the order of keys
print("\n=== OrderedDict ===")
""" This allows us to keep the order of items added """
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)
ordered_dict_2 = OrderedDict()
ordered_dict_2["person"] = "Brian"
ordered_dict_2["animal"] = "Cat"
ordered_dict_2["vehicle"] = "Ferrari"
print(ordered_dict_2)

# Using defaultdict to provide default values for keys
print("\n=== defaultdict ===")
"""
This will provide a default value if the key hasn't been added yet.
"""
default_dict = defaultdict(bool)
default_dict['a'] = 1
default_dict['b'] = 2
print(default_dict['a'])
print(default_dict['c'])
print(default_dict['d'])

# Using deque for a double-ended queue
print("\n=== deque ===")
""" Double Ended queue, which will allow us to access from both ends efficiently. """
d = deque([1, 2, 3])
d.append(4)  # add to the right
print(d)  # Output: deque([1, 2, 3, 4])
d.appendleft(0)  # add to the left
print(d)  # Output: deque([0, 1, 2, 3, 4])
d.pop()  # remove from the right
print(d)  # Output: deque([0, 1, 2, 3])
d.popleft()  # remove from the left
print(d)  # Output: deque([1, 2, 3])
