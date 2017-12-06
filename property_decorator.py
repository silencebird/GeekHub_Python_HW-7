class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '%s.%s@email.com' % self.first, self.last

    @property
    def fullname(self):
        return '%s %s'% self.first, self.last