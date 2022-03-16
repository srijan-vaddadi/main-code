class Account:

    def __init__(self, type):
        self._type = type
        self._money = 0

    def set_type(self, type):
        self._type = type

    def deposit(self, deposit):
        if deposit > 0:
            self._money = self._money + deposit

    def withdraw(self, withdraw):
        if 0 < withdraw <= self._money:
            self._money = self._money - withdraw

    def get_balance(self):
        return self._money
