# testing out a range what if we wanted something that would loop 10 times
#for i in 10:
#    print(i)
# getting an error because an int is not iterable

# start - the index the range starts at
# stop - the index the range stops at
# step - how much the index increases as iterated through
# Range[ start, stop, step ]
for i in range(0, 10, 1):
    print(i)
    
print('\n==========\n')
    
# Python is smart enough to know that ranges always start at 0 and increase by 1 unless otherwise specified
for i in range(10):
    print(f'{i} - shortened')
    
print('\n==========\n')
    
# make the range start at 5
for i in range(5, 10):
    print(f'{i} - start at 5')
