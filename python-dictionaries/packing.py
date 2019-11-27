def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)

# positional arguments - have to be passed in a specific order
print_teacher('Ashley', 'Teacher', 'Python')
print('==========')


# function declaration is using packing
# more flexible because any number of arguments can be passed to the function
# kwargs = key word arguments
def print_teacher2(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
        
# variable names have to match parameter names
print_teacher2(name='Ashley', job='Teacher', topic='Python')
print('----------')
print_teacher2(name='Ashley', job='Teacher', topic='Python', second_topic='JavaScript')

print('\n==========')
print('UNPACKING')
print('==========\n')

# CONSIDER THIS CODE:
# dictionary holds 3 key:value pairs
teacher = {
  'name':'Ashley',
  'job':'Instructor',
  'topic':'Python'
}

def print_teacher3(name, job, topic):
    print(name)
    print(job)
    print(topic)
    
# in order to pass all of the key:value pairs to the
# print_teacher3 function we need to unpack the dictionary
print_teacher3(**teacher)
# its the ** that unpacks our dictionaries key:value pairs into three keywordarguments