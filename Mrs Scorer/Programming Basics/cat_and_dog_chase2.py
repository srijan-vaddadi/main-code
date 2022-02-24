import animal_part_2
from random import randint

dragon = animal_part_2.Animal('Smaug')
dragon.move(1, 1)
cat = animal_part_2.Animal('Fluffy')
cat.move(1, 1)
dog = animal_part_2.Animal('Jimmy')

while dog.locate()[0] != cat.locate()[0] or dog.locate()[1] != cat.locate()[1]:
    cat.move(randint(-3, 3), randint(-3, 3))
    dragon.locate()

    if dog.locate()[0] < cat.locate()[0] or dog.locate()[1] < cat.locate()[1]:
        dog.move(randint(0, 1), randint(0, 1))
    if dog.locate()[0] > cat.locate()[0] or dog.locate()[1] > cat.locate()[1]:
        dog.move(randint(-1, 0), randint(-1, 0))

    if dragon.locate()[0] < dog.locate()[0] or dragon.locate()[1] < dog.locate()[1]:
        dragon.move(randint(0, 1), randint(0, 1))
    if dragon.locate()[0] > dog.locate()[0] or dragon.locate()[1] > dog.locate()[1]:
        dragon.move(randint(-1, 0), randint(-1, 0))

    if dog.locate() == dragon.locate():
        dog.death()
        print('Fluffy wins')
        break

    if cat.locate() == dog.locate():
        cat.death()
        print('Jimmy wins')
        break
