class Root(object):

    def __init__(self, origin):
        self.origin = origin
        self.p1 = None
        self.p2 = None

    def set_p(self):
        self.p1 = self.origin.get("p1")
        self.p2 = self.origin.get("p2")


class Branch(Root):
    def __init__(self, origin):
        super(Branch, self).__init__(origin)
        super(Branch, self).set_p()


if __name__ == '__main__':
    a = Root({"p1": "a", "p2": "b"})
    print a.p1  # 输出为None
    b = Branch({"p1": "a", "p2": "b"})
    print b.p1  # 输出为a
