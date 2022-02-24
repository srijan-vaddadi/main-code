import animal_part_2
from random import randint

dragon = animal_part_2.Animal('Smaug')
dragon.move(-1, -1)
cat = animal_part_2.Animal('Fluffy')
cat.move(1, 1)
dog = animal_part_2.Animal('Jimmy')
obj1 = animal_part_2.Animal('Obj1')
obj2 = animal_part_2.Animal('Obj2')
obj3 = animal_part_2.Animal('Obj3')
obj4 = animal_part_2.Animal('Obj4')
obj5 = animal_part_2.Animal('Obj5')


while dog.locate()[0] != cat.locate()[0] or dog.locate()[1] != cat.locate()[1]:
    cat.move(randint(-3, 3), randint(-3, 3))
    dragon.locate()
    obj1.teleport(randint(-50, 50), randint(-50, 50))
    obj2.teleport(randint(-50, 50), randint(-50, 50))
    obj3.teleport(randint(-50, 50), randint(-50, 50))
    obj4.teleport(randint(-50, 50), randint(-50, 50))
    obj5.teleport(randint(-50, 50), randint(-50, 50))

    if dog.locate()[0] < cat.locate()[0] or dog.locate()[1] < cat.locate()[1]:
        dog.move(randint(0, 1), randint(0, 1))
    if dog.locate()[0] > cat.locate()[0] or dog.locate()[1] > cat.locate()[1]:
        dog.move(randint(-1, 0), randint(-1, 0))

    if dragon.locate()[0] < dog.locate()[0] or dragon.locate()[1] < dog.locate()[1]:
        dragon.move(randint(0, 1), randint(0, 1))
    if dragon.locate()[0] > dog.locate()[0] or dragon.locate()[1] > dog.locate()[1]:
        dragon.move(randint(-1, 0), randint(-1, 0))

    if dog.locate() == obj1.locate() or obj2.locate() or obj3.locate() or obj4.locate() or obj5.locate():
        print('Fluffy hit an object')
        print('Jimmy wins')
        dog.death()
        break
    if cat.locate() == obj1.locate() or obj2.locate() or obj3.locate() or obj4.locate() or obj5.locate():
        print('Jimmy hit an object')
        print('Fluffy wins')
        cat.death()
        break

    if dog.locate() == dragon.locate():
        dog.death()
        print('Fluffy wins')
        break

    if cat.locate() == dog.locate():
        cat.death()
        print('Jimmy wins')
        break
