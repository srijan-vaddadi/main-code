import animal_part_2
from random import randint

cat = animal_part_2.Animal('Fluffy')
cat.move(1, 1)
dog = animal_part_2.Animal('Jimmy')

while dog._position != cat._position:
    cat.move(randint(-3, 3), randint(-3, 3))
    print(cat.locate())
    if dog._position[0] < cat._position[0]:
        dog.move(1, 0)
    elif dog._position[0] > cat._position[0]:
        dog.move(-1, 0)
    if dog._position[1] < cat._position[1]:
        dog.move(0, 1)
    elif dog._position[1] > cat._position[1]:
        dog.move(0, -1)
    print(dog.locate())
if cat._position == dog._position:
    cat.death()