import animal_part_2
from random import randint

dragon = animal_part_2.Animal('Smaug')
dragon.move(-1, -1)
cat = animal_part_2.Animal('Fluffy')
cat.move(1, 1)
dog = animal_part_2.Animal('Jimmy')

obj1 = animal_part_2.Object('Obj1')
obj2 = animal_part_2.Object('Obj2')
obj3 = animal_part_2.Object('Obj3')
obj4 = animal_part_2.Object('Obj4')
obj5 = animal_part_2.Object('Obj5')

obj1.teleport(randint(-10, 10), randint(-10, 10))
obj2.teleport(randint(-10, 10), randint(-10, 10))
obj3.teleport(randint(-10, 10), randint(-10, 10))
obj4.teleport(randint(-10, 10), randint(-10, 10))
obj5.teleport(randint(-10, 10), randint(-10, 10))

while dog.locate()[0] != cat.locate()[0] or dog.locate()[1] != cat.locate()[1]:

    cat.move(randint(-3, 3), randint(-3, 3))

    if dog.locate()[0] < cat.locate()[0] or dog.locate()[1] < cat.locate()[1]:
        dog.move(randint(0, 1), randint(0, 1))
    if dog.locate()[0] > cat.locate()[0] or dog.locate()[1] > cat.locate()[1]:
        dog.move(randint(-1, 0), randint(-1, 0))
    dog.location()

    if dragon.locate()[0] < dog.locate()[0] or dragon.locate()[1] < dog.locate()[1]:
        dragon.move(randint(0, 1), randint(0, 1))
    if dragon.locate()[0] > dog.locate()[0] or dragon.locate()[1] > dog.locate()[1]:
        dragon.move(randint(-1, 0), randint(-1, 0))
    dragon.location()

    if dog.locate() == obj1.location() or dog.locate() == obj2.location() or dog.locate() == obj3.location()\
            or dog.locate() == obj4.location() or dog.locate() == obj5.location():
        print('Jimmy hit an object')
        dog.death()
        print('Fluffy wins')
        break
    if cat.locate() == obj1.location() or cat.locate() == obj2.location() or cat.locate() == obj3.location()\
            or cat.locate() == obj4.location() or cat.location() == obj5.location():
        print('Fluffy hit an object')
        cat.death()
        print('Jimmy wins')
        break

    if dog.location() == dragon.location():
        dog.death()
        print('Fluffy wins')
        break
    if cat.location() == dog.location():
        cat.death()
        print('Jimmy wins')
        break
