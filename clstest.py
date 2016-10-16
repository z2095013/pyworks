class Py2code:
    ''' Python 2.x string and unicode module'''

    def __init__(self):
        pass


    def to_unicode(self, unicode_or_str):
        if isinstance(unicode_or_str, str):
            self.value = unicode_or_str.decode('utf-8')
        else:
            self.value = unicode_or_str
        return self.value


    def to_str(self, unicode_or_str):
        if isinstance(unicode_or_str, unicode):
            self.value = unicode_or_str.encode('utf-8')
        else:
            self.value = unicode_or_str
        return self.value




    ''' file operation

    with open('random.bin', 'wb') as f:
        f.write(os. urandom(10))

    '''
