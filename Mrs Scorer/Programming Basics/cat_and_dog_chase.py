import animal_part_1
from random import randint

cat = animal_part_1.Animal('Fluffy')
cat.move(1, 1)
dog = animal_part_1.Animal('Jimmy')

while dog.position != cat.position:
    cat.move(randint(-3, 3), randint(-3, 3))
    print(cat.locate())
    if dog.position[0] < cat.position[0]:
        dog.move(1, 0)
    elif dog.position[0] > cat.position[0]:
        dog.move(-1, 0)
    if dog.position[1] < cat.position[1]:
        dog.move(0, 1)
    elif dog.position[1] > cat.position[1]:
        dog.move(0, -1)
    print(dog.locate())
if cat.position == dog.position:
    cat.death()
