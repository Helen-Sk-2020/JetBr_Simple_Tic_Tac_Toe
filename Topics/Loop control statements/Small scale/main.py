numb = []
while True:
    x = input()
    if x == '.':
        break
    else:
        numb.append(float(x))
print(min(numb))
