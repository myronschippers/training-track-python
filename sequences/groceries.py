# All sequences are iterable they can be looped over sequences are no exception
# For in Loop - a way to perform an action on every item in a sequence
my_name = 'Myron'
for letter in my_name:
    print(letter)

print('\n==========\n')

# groceries list was provided
groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']

count = 1
# iterate over the list and print out the grocery items
for food in groceries:
    # f' string can be used in order to add variables to strings
    print(f'{count}. {food}')
    count+=1

print('\n==========\n')

# iterate over groceries and use the enumerate function to access index but notice it starts at 
for index, food in enumerate(groceries):
    # f' string can be used in order to add variables to strings
    print(f'{index}. {food}')

print('\n==========\n')

# iterate over groceries and use the enumerate function to access a tupol of index, food
for index, food in enumerate(groceries, 1):
    print(f'{index}. {food}')

print('\n==========\n')

# start count at 20
for index, food in enumerate(groceries, 20):
    print(f'{index}. {food}')
