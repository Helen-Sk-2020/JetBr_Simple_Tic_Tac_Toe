guests = []
counter = 0
while True:
    name = input()
    if name == '.':
        break
    else:
        guests.append(name)
        counter += 1
print(guests)
print(counter)
