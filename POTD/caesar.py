
cipher = input('Enter your cipher text: ')
cipher = cipher.lower()
cipher = (list(cipher))
decoded = ''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
    , 'w', 'x', 'y', 'z']

alphabet_2 = ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
    , 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l']

my_dict = dict(zip(alphabet_2, alphabet))

for x in cipher:
    if x in my_dict.keys():
        decoded = decoded + str((my_dict[x]))
    else:
        decoded = decoded + x
print('The decoded phrase is: ' + decoded)























