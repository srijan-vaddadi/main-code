import animal_part_2
from random import randint

cat = animal_part_2.Animal('Fluffy')
cat.move(1, 1)
dog = animal_part_2.Animal('Jimmy')

while dog.locate()[0] != cat.locate()[0] or dog.locate()[1] != cat.locate()[1]:
    cat.move(randint(-3, 3), randint(-3, 3))
    if dog.locate()[0] < cat.locate()[0]:
        dog.move(1, 0)
    elif dog.locate()[0] > cat.locate()[0]:
        dog.move(-1, 0)
    if dog.locate()[1] < cat.locate()[1]:
        dog.move(0, 1)
    elif dog.locate()[1] > cat.locate()[1]:
        dog.move(0, -1)
if cat.locate() == dog.locate():
    cat.death()
