class A(object):

    def __init__(self, origin):
        self.origin = origin
        self.p1 = None

    def __set_p(self):
        self.p1 = self.origin.get("p1")

    def set_p(self):
        self.__set_p()
        print "A.set"


class B(A):
    def __init__(self, origin):
        super(B, self).__init__(origin)
        super(B, self).set_p()

    def set_p(self):
        pass


if __name__ == '__main__':
    b = B({"p1": "a"})  # A.set
    print b.p1   # a
    b.set_p()   # do nothing
