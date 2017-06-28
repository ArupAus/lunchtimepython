# Session 3: Python Data Types

```py
# calculate length of list
def list_length(somelist):
    return(len(somelist))
    
#calculate sum of all numbers
def list_sum(somelist):
    return(sum(somelist))

# maximum
def list_max(somelist):
    return(max(somelist))

# minimum
def list_min(somelist):
    return(min(somelist))
    
# mean
def list_mean(somelist):
    return(sum(somelist)/len(somelist))

# square map
def square_map(itemList):
    squares = []
    for item in itemList:
        squares.append(item**2)
    
    return(squares)
  
# apppend check
def my_append(somelist, animal):
    if not animal in somelist:
        somelist.append(animal)
        return(somelist)
    else:
        return(somelist)
  
# pretty print
def pprint(dictionary):
    print('{')
    for key, value in dictionary.items():
        print('\t{0}: {1}'.format(key, value))
    print('}')

# into the wild
def fill_backpack(itemDictionary):
    # set up an empty bag
    backpack = {
        'items': [],
        'weight': 0
        }

    weight_limit = 7

    for item in itemDictionary:
        # check if the item fits in the backpack
        if item['weight'] + backpack['weight'] < weight_limit:
            backpack['items'].append(item['name']) # add item to backpack
            backpack['weight'] += item['weight'] # update the weight of the backpack
    
    print('{')
    print('items:', backpack['items'])
    print('weight:', backpack['weight'])
    print('}')
```