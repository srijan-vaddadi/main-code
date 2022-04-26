class Account:

    def __init__(self, name):
        self._name = name
        self._money = 0

    def set_type(self, name):
        self._name = name

    def set_money(self):
        config_folder = "C:/Users/srija/srijan_cs"
        config_file = open(self._name, config_folder)
        self._money = config_file.readlines()

    def deposit(self, deposit):
        if deposit > 0:
            self._money = self._money + deposit

    def withdraw(self, withdraw):
        if 0 < withdraw <= self._money:
            self._money = self._money - withdraw

    def get_balance(self):
        return self._money
