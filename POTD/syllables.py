# Aadil Abbas (aa4zw)

first = str(input('Please give me a word: '))
word = list(first)
vowels = ('a', 'e', 'i', 'o', 'u', 'y')
syllables = 0
count = 0
final_syllable = 0
last_position = len(word) - 1
last_letter = (word[last_position])

for letter in word:
    if letter in vowels:
        count += 1
        final_syllable = syllables
        syllables += 1
        if count > 1:
            syllables = final_syllable
    if letter not in vowels:
        count = 0

if last_letter == vowels[1]:
        syllables -= 1
        if syllables == 0:
            syllables += 1


print('The word ' + first + ' has ' + str(syllables) + ' syllables.')













