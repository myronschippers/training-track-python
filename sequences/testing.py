docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'

search = 'tuple'

if search in docs:
    # do something if true
    print(f'{search} is here')
else: 
    # do something else
    print(f'{search} is not here')
    
if search not in docs:
    print(f'{search} is not here')
else:
    print(f'{search} is here')