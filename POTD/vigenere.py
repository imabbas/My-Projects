
my_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21
    , 'w':22, 'x':23, 'y':24, 'z':25}

my_dict2 = {y:x for x,y in my_dict.items()}
print(my_dict2)

my_list = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
    , 'w', 'x', 'y', 'z')


def letter_to_index(letter):
    if letter in my_dict:
        return int(my_dict[letter])
    else:
        return -1

def index_to_letter(index):
    if index in my_dict2:
        return my_dict2[index]
    else:
        return '?'

def vigenere_encrypt(plain_letter, key_letter):
    if plain_letter not in my_list:
        return plain_letter
    if key_letter not in my_list:
        return plain_letter
    else:
        a = my_dict[key_letter]
        b = my_dict[plain_letter]
        if a + b > 25:
            c = (a + b)-26
            return my_dict2[c]
        elif a + b >= 0 and a + b <= 25:
            return my_dict2[a+b]

def vigenere_decrypt(cipher_letter, key_letter):
    if cipher_letter not in my_list:
        return cipher_letter
    if key_letter not in my_list:
        return cipher_letter
    else:
        a = my_dict[key_letter]
        b = my_dict[cipher_letter]
        if b-a < 0:
            c = (b-a)+26
            return my_dict2[c]
        elif b-a >= 0 and b-a <= 25:
            return my_dict2[b-a]

# def encrypt(plaintext, key):
#     plaintext = list(plaintext)
#     key = list(key)
#     for char in key:
#         for letter in plaintext:
#             return vigenere_encrypt(letter, char)

def encrypt(plaintext, key):
    plaintext2 = plaintext
    key2 = key
    encription = ""
    plaintext = plaintext.lower()
    plaintext = list(plaintext)
    key = key.lower()
    key = list(key)
    for letter in plaintext:
        position = plaintext.index(letter)
        char = key[position]
        encription = encription + vigenere_encrypt(letter, char)
    print('Plaintexts: '+ plaintext2)
    print('EncryptKey: '+ key2)
    print('Ciphertext: '+ encription)

def decrypt(ciphertext, key):
    ciphertext2 = ciphertext
    key2 = key
    decryption = ""
    ciphertext = ciphertext.lower()
    ciphertext = list(ciphertext)
    key = key.lower()
    key = list(key)
    for letter in ciphertext:
        position = ciphertext.index(letter)
        char = key[position]
        decryption = decryption + vigenere_decrypt(letter, char)
    print('Ciphertexts: '+ ciphertext2)
    print('DecryptKey: '+ key2)
    print('Plaintext: '+ decryption)












