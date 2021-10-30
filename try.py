class demo:
    def demo(self, name):
        self.name=name
        #self.company=company
        print('hi {}, welcome home'.format(self.name))

class demo2:
    def demo(self, name):
        self.name=name
        #self.company=company
        return name

D=demo()
D2=demo2()

D.demo(D2.demo('swapnil'))

