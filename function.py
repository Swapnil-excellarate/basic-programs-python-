## decorater program

def welcome(function):
    def sub_welcome(a=5, b=2):
        if a>b:
            print('welcome to excellarate')
            function('a is greter the b')
            print('thank you been here')
        else:
            print('b is greter')
    return sub_welcome()

if __name__=="__main__":
    welcome(print)