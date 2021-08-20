def initialDeco(function):

    def Deco():
        print('welcome to word')
        function()
        print('thank you')
    return Deco()

@initialDeco
def show():
    print('Hello user')