# word = input()
# print("Palindrome" if word[::-1] == word else "Not palindrome")

word = input()
length = len(word)
count = 0
result = ''

while True:
    if word[::+1] == word[::-1]:
        count += 1
        if count > length / 2:
            break
        result = 'Palindrome'
    else:
        result = 'Not palindrome'
        break
print(result)
