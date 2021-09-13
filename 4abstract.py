from abc import ABC, abstractclassmethod

class computer(ABC):

    @abstractclassmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print('IT Running')
        W.process()
class whiteboard(computer):
    def process(self):
        print('write the code')
        

W=whiteboard()

c1=laptop()
c1.process()