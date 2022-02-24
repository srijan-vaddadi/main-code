import animal_part_2
from random import randint

cat = animal_part_2.Animal('Fluffy')
cat.move(1, 1)
dog = animal_part_2.Animal('Jimmy')

while dog.locate() != cat.locate():
    cat.move(randint(-3, 3), randint(-3, 3))
    print(cat.locate())
    if dog.locate < cat.locate():
        dog.move(1, 0)
    elif dog.locate() > cat.locate():
        dog.move(-1, 0)
    if dog.locate() < cat.locate():
        dog.move(0, 1)
    elif dog.locate() > cat.locate():
        dog.move(0, -1)
    print(dog.locate())
if cat.locate() == dog.locate():
    cat.death()
