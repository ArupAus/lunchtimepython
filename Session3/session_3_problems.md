# Session 3: Python Data Types

## A little theory

Try to answer the questions then use the python console to check. 

For the following questions assume `numbers = [0,1,2,3,4]`

- What is `[]`?
- What does `numbers[-1]` evaluate to?
- What does `numbers.append(9)` make the list `numbers` look like?
- What does `numbers.insert(2,9)` make the list `numbers` look like?

For the following questions assume `names = ["Alex", "Mia", "John", "Laura", "Joyce"]`

- What does `names.pop()` *return* and what does the list `names` become?
- What does `names.remove("mia")` *return* and what does the list `names` become?

For the following questions assume `person = {"name":"Alex", "age":27, "height":158}`

- How would you change the value associated with the key `"name"` from "Alex" to "John"?
- How would you add the key-value pair `{"graduate":True}` to the dictionary `person`?
- What would `list(person.keys())` look like?


## Data analysis

For the following list:
```py
# Copy and paste into your script
temperatures = [12,35,32,13,6,-23,-5,35,-42,-24,45,23,-64,8,2,-4]
```

- Calculate the length of the list `temperatures`
- Calculate the sum of all temperatures
- Find the maximum temperature
- Find the minimum temperature
- Calculate the mean temperature (mean = sum of temperatures divided by the number of temperature measurements)

*HINT:* The `for` loop is very useful when dealing with lists. Below is an example of using a `for` loop to determine the longest name in a list of names.

```py
names = ["Alex", "Mia", "John", "Laura", "Joyce"]
longest_name = "" # initialise with an empty string

for name in names:
	if len(name) > len(longest_name):
		longest_name = name

print("The longest name is: " + longest_name)
# The longest name is Laura
```

Build a separate function for each of the tasks above to be submitted to the marker bot:

```py
def list_length(a_list):
	return answer
```

```py
def list_sum(a_list):
	return answer
```

```py
def list_max(a_list):
	return answer
```

```py
def list_min(a_list):
	return answer
```

```py
def list_mean(a_list):
	return answer
```

## Square map

Write a function called `square_map` that takes in a list of numbers (integers or floats) and returns a list of the same length only each element has been squared.

Sample input/output:
```
>>> numbers = [1,2,3,5]
>>> square_map(numbers)
[1, 4, 9, 25]
```

Submit you answer to the marker bot using the function name below.
```py
def square_map(a_list):
	return squared_list
```

**Bonus points:** Complete the problem using a [*list comprehension*](http://www.diveintopython3.net/comprehensions.html#listcomprehension).

## Append Check

Write a function called `my_append` that adds an element to a list provided that element is not already in the list.

Sample input/output:
```
>>> animals = ["cat", "dog", "elephant", "pig"]
>>> more_animals = my_append(animals, "zebra")
>>> print(more_animals)
["cat", "dog", "elephant", "pig", "zebra"]
```

Submit your function to markerBot as shown:
```py
def my_append(a_list, element):
	# add your function her
	return appended_list
```

## Into the wild

Instead of going to work tomorrow you decide to go on an adventure. You have a number of items that you would like to take. However, you can only carry 7kg. Your job is to pack you bag with as many items as you can while ensuring that the weight of the backpack does not exceed 6kg.

It is best to represent the backpack as a dictionary:

```py
backpack = {
	items:	["toothbrush", "sandwhich", "bon soy", "book on python"]
	weight:	2.750}
```

Below is a list of your items that you could possibly take where each item is represented as a dictionary:

```py
# copy and paste into your code if you like.
items = [
	{"name": "tooth brush", "weight": 0.050},
	{"name": "sandwhich", "weight": 0.100},
	{"name": "iPod", "weight": 0.250},
	{"name": "tomahawk", "weight": 2.000},
	{"name": "bon soy", "weight": 1.000},
	{"name": "sling shot", "weight": 0.800},
	{"name": "book on python", "weight": 1.600},
	{"name": "water", "weight": 1.800},
	{"name": "tissues",  "weight": 0.150},
	{"name": "first aid kit", "weight": 0.750},
	{"name": "flint", "weight": 1.075},
	{"name": "magnifying glass", "weight": 0.450}
]
```

Build a function called `fill_backpack` that takes in the list of items as a sinlge argument and returns the backpack dictionary.

```py
def fill_backpack(items):
	return backpack
```
