# Aadil Abbas (aa4zw)

number = input('Type a credit card number (just digits): ')
credit = number
number = list(number)

x = -1
sum = 0
sum2 = 0
list2 = ""
list3 = ""
number2 = number

while x >= int(-len(number)):
    list2 = list2 + number[x]
    sum = sum + int(number[x])
    x = x - 2


if len(number) % 2 == 0:
    i=0
else:
    i=1

while i < len(number):
    number[i] = int(number[i])
    number[i] = (number[i])*2
    number[i] = str(number[i])
    list3 = list3 + number[i]
    i = i + 2

for char in list3:
    sum2 = sum2+int(char)

final_sum = sum + sum2

if final_sum % 10 == 0:
    print("Yes, " + credit + " is a valid credit card number")
else:
    print(credit + " is not a valid credit card number")





