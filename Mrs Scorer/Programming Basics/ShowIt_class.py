class ShowIt:
    """List display"""

    def __init__(self, name='', seq=[]):
        if seq:
            self._name = name
            self._seq = seq
        else:
            self._name = 'Visible spectrum'
            self._seq = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
        self._seqlen = len(self._seq)
        self._i = -1
