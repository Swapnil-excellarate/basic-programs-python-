## decorater program

def welcome(function):
    def sub_welcome():
        print('welcome to excellarate')
        print(function)
        print('thank you been here')
    return sub_welcome()

if __name__=="__main__":
    welcome('hope you are fine in the pandamic')