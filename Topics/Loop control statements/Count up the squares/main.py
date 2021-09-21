import math

number = int(input())
sum_ = 0
sum_squares = 0

while True:
    sum_ += number
    sum_squares += math.pow(number, 2)
    if sum_ == 0:
        break
    number = int(input())

if number == 0:
    print(0)
else:
    print(round(sum_squares))
