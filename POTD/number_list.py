num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
num3 = int(input('Number 3: '))
num4 = int(input('Number 4: '))
num5 = int(input('Number 5: '))

list = [num1, num2, num3, num4, num5]
print('')
print('You entered: ' + str(list))
average = sum(list)/len(list)
print('The average is: ' + str(average))
range = (max(list) - min(list))
print('The range is: ' + str(range))
remove = int(input('Which item do you want to remove?: '))
print('')
list.remove(remove)
print('The new list has the following values: ' + str(list))
average = sum(list)/len(list)
print('The average is: ' + str(average))
range = (max(list) - min(list))
print('The range is: ' + str(range))









