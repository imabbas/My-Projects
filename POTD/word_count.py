word_list = str(input('Give me 10 words!: '))
words = word_list.lower()
words = words.split()

a = 0
for word in words:
    if word == words[0]:
        a = a + 1
b = 0
for word in words:
    if word == words[1]:
        b = b + 1
c = 0
for word in words:
    if word == words[2]:
        c = c + 1
d = 0
for word in words:
    if word == words[3]:
        d = d + 1
e = 0
for word in words:
    if word == words[4]:
        e = e + 1
f = 0
for word in words:
    if word == words[5]:
        f = f + 1
g = 0
for word in words:
    if word == words[6]:
        g = g + 1
h = 0
for word in words:
    if word == words[7]:
        h = h + 1
i = 0
for word in words:
    if word == words[8]:
        i = i + 1
j = 0
for word in words:
    if word == words[9]:
        j = j + 1

my_dict = {words[0]: a, words[1]: b, words[2]: c, words[3]: d, words[4]: e, words[5]: f, words[6]: g, words[7]: h,
           words[8]: i, words[9]: j}
count_word = str.lower(input('Which word count do you want?: '))
new_word = str(count_word.capitalize())

if count_word in my_dict:
    print('The word \'' + str(count_word) + '\' appears ' + str(my_dict[count_word]) + ' times.')
else:
    print('The word \'' + str(count_word) + '\' appears no times.')








