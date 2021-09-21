# import math
cafe_name = []
cats_number = []
while True:
    cafe = input()
    if cafe == "MEOW":
        break
    cafe = cafe.split()
    cafe_name.append(cafe[0])
    cats_number.append(int(cafe[1]))
print(cafe_name[cats_number.index(max(cats_number))])
