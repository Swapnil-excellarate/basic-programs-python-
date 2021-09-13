
n=int(input('enter any number between 4 to 6:-'))
def backword_triangle():
    for i in range(n,0,-1):
        for j in range(i):
            print(j, end="")
            j+=1
        print()

def forword_triangle():
    for i in range(0,n):
        for j in range(0, i):
            print(i, end="")
            j+=1
        print()

def square():
    for i in range(n):
        for j in range(n):
            print(i, end="")
        print()

def pyramid():
    for i in range(n):
        for j in range(0,n-1-i):
            print(end=" ")
        for j in range(0, i+1):
            print(j, end=" ")
        print()

def Inverted_Pyramid():
    for i in range(1, n+1):
        for j in range(i, n+1):
            print(i, end=" ")
        print()

def Unique_Pyramid():
    for i in range(1, n):
        for j in range(1, i):
            print(j, end="")
        for j in range(i, 0, -1):
            print(j, end="")
        print()

def even_pyramid():
    for i in range(n, 0,-2):
        for j in range(i,0,-2):
            print(j, end=" ")
        print()

def errorhander():
    return "Invalid choise"

print('To display patter you need to choose one of them--->')
print('''
    1. backword traing
    2. forword traing 
    3. square
    4. pyramid
    5. Inverted Pyramid
    6. Unique Pyramid
    7. Even Pyramid
''')


choise=int(input('Enter which pattern you want to display :'))

operation={
    1: backword_triangle,
    2: forword_triangle,
    3: square,
    4: pyramid,
    5: Inverted_Pyramid,
    6: Unique_Pyramid,
    7: even_pyramid
}

result= operation.get(choise, errorhander)()
# operation= [backword_triangle, forword_triangle, square]
# result=operation[choise-1]()


print(result)
# a=square()
# print(a)

