count = 0
sum_ = 0
while True:
    number = input()
    if number == '.':
        break
    count += 1
    sum_ += int(number)
    x = sum_ / count

print(x)
