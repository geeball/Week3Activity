name = input('Enter the students\'s name: ')

mark_1 = int (input ('Enter First Result: '))
mark_2 = int (input ('Enter Second Result: '))
mark_3 = int (input ('Enter Third Result: '))
mark_4 = int (input ('Enter Fourth Result: '))
mark_5 = int (input ('Enter Fifth Result: '))

total_marks = mark_1 + mark_2 + mark_3 + mark_4 + mark_5

print()
print('Total mark for ' + name + ' is: ' + str (total_marks))