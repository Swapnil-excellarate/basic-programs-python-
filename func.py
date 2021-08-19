class car():
    def __init__(self, door, window, enginetype):
        self.doors=door
        self.window=window
        self.enginetype=enginetype
    def engine(self):
        return 'engine type is'.format(self.enginetype)

if __name__=='__main__':
    car1=car(4,4,'petrol')
    print(car1)