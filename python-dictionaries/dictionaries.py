course = {'teacher':'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginner'}
print("Original dictionary:")
print(course)
print("==========\n")

# changing a key value in the course dictionary
course['teacher'] = 'Treasure'
print('\nAdjusted "teacher":')
print(course)
print("==========\n")

# changing the value associated with the level key
course['level'] = 'Intermediate'
print('\nAdjusted "level":')
print(course)
print("==========\n")

# adding a new key value pair that was not already on the dictionary
course['stages'] = 2
print('\nAdding new key value pair:')
print(course)
print("==========\n")

# adding a new key value pair that was not already on the dictionary
course['track'] = 'Data Science'
print('\nAdding "track" to course:')
print(course)
print("==========\n")

# removing "stages" from the "course" dictionary
del(course['stages'])
print('\nRemoved "stages":')
print(course)
print("==========\n")

# iterating over a dictionary
print("\nIterate through dictionary using loop:")
for itemKey in course:
    itemValue = course[itemKey]
    print("Course Item:")
    print("  > {}: {}".format(itemKey, itemValue))
    print("  ----------")
print("==========\n")
    
# method to get all key value pairs
print("\nGet all key / value pairs:")
print(course.items())
for item in course.items():
    print("  item: {}".format(item))
    print("  ----------")

# unpacking toopul(s)
for key, value in course.items():
    print("  KEY:", key)
    print("  VALUE:", value)
    print("  ----------")
print("==========\n")
