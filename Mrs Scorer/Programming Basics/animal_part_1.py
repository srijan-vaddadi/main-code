# Animal class - part 1
# A basic class. Not fully encapsulated.

class Animal(object):
    """An animal class"""

    def __init__(self, name):
        self.legs = 4
        self.awake = True
        self.position = [0, 0]
        self.name = name
        self.alive = True

    def death(self):
        self.alive = not self.alive
        if self.alive:
            state = 'is alive'
        else:
            state = 'is dead'
        print(self.name, state)

    def toggle_sleep(self):
        """Toggles animal between awake and asleep"""
        self.awake = not self.awake
        if self.awake:
            state = 'is awake.'
        else:
            state = 'is asleep'
        print(self.name, state)

    def move(self, a, b):
        """Moves animal from current position by
        a in x-direction, b in y-direction"""
        try:
            self.position[0] += a
            self.position[1] += b
            return True
        except:
            print('Invalid a,b:', (a, b))
            print('Postion left unchanged')
            return False

    def locate(self):
        print('The animal {0} is at {1}, {2}.'.format(self.name,
                                                      self.position[0],
                                                      self.position[1]))
        return self.position


cat = Animal('Fluffy')
dog = Animal('Jimmy')
dragon = Animal('Smaug')
print(dragon.legs)
dragon.legs = 2
print(dragon.legs)
