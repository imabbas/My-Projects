# Aadil Abbas (aa4zw)

integer = (int(input('Enter an integer: ')))



roman_numeral = ""
final = str(integer)
my_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900:
    'CM', 1000: "M"}

decimal_value = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

if integer >= 1000:
    roman_1 = integer % 1000
    roman_1 = (integer - roman_1)/1000
    while roman_1 > 0:
        roman_numeral = roman_numeral + "M"
        integer = integer - 1000
        roman_1 = roman_1 - 1

if integer >= 900:
    roman_2 = integer % 900
    roman_2 = (integer - roman_2)/900
    while roman_2 > 0:
        roman_numeral = roman_numeral + "CM"
        integer = integer - 900
        roman_2 = roman_2 - 1

if integer >= 500:
    roman_3 = integer % 500
    roman_3 = (integer - roman_3)/500
    while roman_3 > 0:
        roman_numeral = roman_numeral + "D"
        integer = integer - 500
        roman_3 = roman_3 - 1

if integer >= 400:
    roman_4 = integer % 400
    roman_4 = (integer - roman_4)/400
    while roman_4 > 0:
        roman_numeral = roman_numeral + "CD"
        integer = integer - 400
        roman_4 = roman_4 - 1

if integer >= 100:
    roman_5 = integer % 100
    roman_5 = (integer - roman_5)/100
    while roman_5 > 0:
        roman_numeral = roman_numeral + "C"
        integer = integer - 100
        roman_5 = roman_5 - 1

if integer >= 90:
    roman_6 = integer % 90
    roman_6 = (integer - roman_6)/90
    while roman_6 > 0:
        roman_numeral = roman_numeral + "XC"
        integer = integer - 90
        roman_6 = roman_6 - 1

if integer >= 50:
    roman_7 = integer % 50
    roman_7 = (integer - roman_7)/50
    while roman_7 > 0:
        roman_numeral = roman_numeral + "L"
        integer = integer - 50
        roman_7 = roman_7 - 1

if integer >= 40:
    roman_8 = integer % 40
    roman_8 = (integer - roman_8)/40
    while roman_8 > 0:
        roman_numeral = roman_numeral + "XL"
        integer = integer - 40
        roman_8 = roman_8 - 1

if integer >= 10:
    roman_9 = integer % 10
    roman_9 = (integer - roman_9)/10
    while roman_9 > 0:
        roman_numeral = roman_numeral + "X"
        integer = integer - 10
        roman_9 = roman_9 - 1

if integer >= 9:
    roman_10 = integer % 9
    roman_10 = (integer - roman_10)/9
    while roman_10 > 0:
        roman_numeral = roman_numeral + "IX"
        integer = integer - 9
        roman_10 = roman_10 - 1

if integer >= 5:
    roman_11 = integer % 5
    roman_11 = (integer - roman_11)/5
    while roman_11 > 0:
        roman_numeral = roman_numeral + "V"
        integer = integer - 5
        roman_11 = roman_11 - 1

if integer >= 4:
    roman_12 = integer % 4
    roman_12 = (integer - roman_12)/4
    while roman_12 > 0:
        roman_numeral = roman_numeral + "IV"
        integer = integer - 4
        roman_1 = roman_12 - 1

if integer >= 1:
    roman_13 = integer % 1
    roman_13 = (integer - roman_13)/1
    while roman_13 > 0:
        roman_numeral = roman_numeral + "I"
        integer = integer - 1
        roman_13 = roman_13 - 1

if int(final) < 1 or int(final) > 3999:
    print('Input must be between 1 and 3999')

else:
    print('In roman numerals, ' + str(final) + " is " + roman_numeral)















