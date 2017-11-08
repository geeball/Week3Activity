Number_of_results = (0, 12)
randint = (0, 12)
results = []
for count in range (0, 12):
    while 1:
        result = int (input('Enter result #' + int (randint (0, 12)) + ':'))
        if result in range (0, 12):
            results.append (result)
            break
        else:
            print ('Invalid. Try again.')
print ('Average is', sum (results) / len (results))