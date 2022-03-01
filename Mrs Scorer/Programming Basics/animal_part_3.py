# Animal class - part 3
# Use of magic methods

class Animal:
    """An animal class"""

    def __init__(self, name):
        self._legs = 4
        self._awake = True
        self._position = [0, 0]
        self._name = name

    def __repr__(self):
        return '<Animal ' + self._name + '>'

    def __str__(self):
        if self._awake:
            wake_str = 'awake'
        else:
            wake_str = 'asleep'
        return 'The animal {0} is {1} at {2}, {3}.'.format(self._name,
                                                           wake_str,
                                                           self._position[0],
                                                           self._position[1])

    def __bool__(self):
        return self._awake

    def __len__(self):
        return len(self._name)

    def set_legs(self, n=4):
        """set number of legs to n"""
        self._legs = n

    def get_legs(self):
        return self._legs

    def set_awake(self, awake=True):
        self._awake = awake

    def get_awake(self):
        return self._awake

    def set_name(self, name=''):
        self._name = name

    def get_name(self):
        return self._name

    def toggle_sleep(self):
        """Toggles animal between awake and asleep"""
        self._awake = not self._awake
        if self._awake:
            state = 'is awake.'
        else:
            state = 'is asleep'
        print(self._name, state)

    def move(self, a, b):
        """Moves animal from current position by
        a in x-direction, b in y-direction"""
        try:
            self._position[0] += a
            self._position[1] += b
            return True
        except:
            print('Invalid a,b:', (a, b))
            print('position left unchanged')
            return False

    def locate(self):
        return self._position


dragon = Animal('Smaug')
print(dir(dragon))
