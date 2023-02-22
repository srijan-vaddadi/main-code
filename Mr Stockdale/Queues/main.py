class Queue:
    def __init__(self, length):
        self._front = 0
        self._rear = -1
        self._size = 0
        self._maxsize = length
        self._q = [None] * length

    def printQueue(self):
        if self._front <= self._rear:
            for i in range(self._front, self._rear+1):
                print(f"{self._q[i]}", end='')

        elif self._front > self._rear:
            for i in range(self._front, self._maxsize):
                print(f"{self._q[i]}", end='')
            for i in range(0, self._rear):
                print(f"{self._q[i]}", end='')
