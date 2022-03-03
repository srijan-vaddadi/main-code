class ShowIt:
    """List display"""

    def __init__(self, name='', seq=[]):
        if seq:
            self._name = name
            self._seq = seq
        else:
            self._name = 'Visible spectrum'
            self._seq = ['Red', 'Orange', 'Yellow', 'Green', 'blue', 'Indigo', 'Violet']
        self._seqlen = len(self._seq)
        self._i = -1

    def __repr__(self):
        return '<ShowIt: ' + self._name + '>'

    def __str__(self):
        text = self._name + ':\n'
        for item in self._seq:
            text += '\t' + item + '\n'
        return text

    def __len__(self):
        return self._seqlen

    def __getitem__(self, n):
        return self._seq[n % self._seqlen]

    def __setitem__(self, n, item):
        self._seq[n % self._seqlen]

    def __iter__(self):
        return self

    def __next__(self):
        self._i += 1
        if self._i >= self._seqlen:
            raise StopIteration
        a = self._seq[:]
        a.sort()
        return a[self._i]

