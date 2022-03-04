import random


class Candidate:
    def __init__(self, name):
        self._name = name
        self._leaningSR = 5
        self._leaningSL = 5
        self._likeS = 5

    def set_name(self, name=''):
        self._name = name

    def get_name(self):
        return self._name

    def set_leaningSR(self):
        self._leaningSR = random.randint(0, 2)
        self._leaningSL = 0

    def set_likeS(self):
        self._likeS = random.randint(0, 10)


class Voters:
    def __init__(self):
        self._lScore = 5

    def set_lScore(self):
        self._lScore = random.randint(0, 10)

    def get_lScore(self):
        return self._lScore

    def vote(self):
        if self._lScore > 4:
            breakpoint()
