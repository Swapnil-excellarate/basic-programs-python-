a=5
b=6

try:
    print('Open the resource')
    print(a/b)
    a=int(input('enter the values = '))

except ValueError as e:
    print('invalid input')
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)

finally:
    print('Resource close')