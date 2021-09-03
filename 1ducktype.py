class developer1:

    def execute():
        print('Python developer')
        print('ML developer')

class developer2:

    def execute():
        print('.Net developer')
        print('Java developer')

class show:

    def code(self, possession):
        possession.execute()

possession=developer1
#possession=developer2
coder= show()

coder.code(possession)