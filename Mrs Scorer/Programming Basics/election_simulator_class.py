import random


class Candidate:
    def __init__(self, name):
        self._name = name
        self._RLS = 5
        self._LLS = 5
        self._likeS = 5

    def set_name(self, name=''):
        self._name = name

    def get_name(self):
        return self._name

    def set_RLS(self):
        self._RLS = random.randint(0, 2)

    def get_RLS(self):
        return self._RLS

    def set_LLS(self):
        self._LLS = random.randint(8, 10)

    def get_LLS(self):
        return self._LLS

    def set_likeS(self):
        self._likeS = random.randint(0, 10)

    def get_likeS(self):
        return self._likeS

