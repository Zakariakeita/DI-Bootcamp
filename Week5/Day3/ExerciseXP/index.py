class MyFunc:
    """def __init__(self):
        pass """

    def FunctionABS( num):
        print(num.__abs__())


    def FunctionInt( num):
        print(num.__int__())


func=MyFunc()
def FunctionInput():
        val=input("Enter Number")
        return val
num=FunctionInput()
print(func.FunctionABS(num))
print(func.FunctionInt(num))
print(func.__doc__)