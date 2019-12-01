# sequence - seq[<start>:<stop>:<step>]
# -- stop, will stop at that position but not include that position value in the result
# seq pos   0 ,  1 ,  2 ,  3 ,  4
# seq =  [ 'a', 'b', 'c', 'd', 'e' ]
# seq[1:4] = [ 'b', 'c', 'd' ]
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(f'get second item from rainbow - {rainbow[1]}')
print('\n==========\n')

# start, at the 1 position / index
# stop, at the 4 position / index
print(f'slice rainbow - {rainbow[1:4]}')
print('\n==========\n')

# by leaving the stop value blank the slice will iterate through the entire list
print(f'slice 4th to End - {rainbow[3:]}')
print('\n==========\n')

# start, when blank starts at 0 position
# stop, when blank the slice will go to the end of the sequence
# step, is the number of items before printed
print(f'slice begining to end (every 2) - {rainbow[::2]}')
print('\n==========\n')

# step, is negative it will count backwards
print(f'slice begining to end (step -1) - {rainbow[::-1]}')
print('\n==========\n')

# slicing works with all sequences even strings
my_name = 'Myron R Schippers Jr'
print(f'slicing string - {my_name[:2]}')
print('\n==========\n')


nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums_partial = nums[0::2]
print(nums_partial)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors_partial = colors[3:6]
print(colors_partial)
