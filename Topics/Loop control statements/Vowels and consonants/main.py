s = input()
vowels = ['a', 'e', 'i', 'o', 'u']
for x in s:
    if x in vowels:
        print('vowel')
    elif x.isalpha():
        print('consonant')
    else:
        break
