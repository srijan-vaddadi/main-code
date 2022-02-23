# Animal class - part 2
# All variables now private,
# accessed through methods.

class Animal():
    '''An animal class'''

    def __init__(self, name):
        self._legs = 4
        self._awake = True
        self._position = [0, 0]
        self._name = name

    def set_legs(self, n=4):
        '''set number of legs to n'''
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
        '''Toggles animal between awake and asleep'''
        self._awake = not self._awake
        if self._awake:
            state = 'is awake.'
        else:
            state = 'is asleep'
        print(self._name, state)

    def move(self, a, b):
        '''Moves animal from current position by
a in x-direction, b in y-direction'''
        try:
            self._position[0] += a
            self._position[1] += b
            return True
        except:
            print('Invalid a,b:', (a, b))
            print('postion left unchanged')
            return False

    def locate(self):
        # print('The animal {0} is at {1}, {2}.'.format(self._name,
        #                                              self._position[0],
        #                                              self._position[1]))
        return self._position

dragon = Animal('Smaug')
dragon.set_legs(2)
print(dragon.get_legs())
print("Hello, World")
print('Hello World2')
