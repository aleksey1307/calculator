def summa(num1,num2):
    sum=num1+num2
    return sum
def minus(num1,num2):
    raz=num1-num2
    return raz
def umnosh(num1,num2):
    proiz=num1*num2
    return proiz
def delit(num1,num2):
    delitel=num1/num2
    return delitel
def Rectangle(side1,side2):
    proizP=side1*side2
    return proizP
def Triangle(side1,side2):
    treugol=side1*side2/2
    return treugol
def  Circle(r):
    krug=3.14*(r**2)
    return krug

while True:
    tip_calculator = str(input("введите калькулятор чисел или калькулятор фигур или стоп"))
    if tip_calculator=="калькулятор чисел":
        operation=str(input("+, -, *, /"))
        num1=int(input("введите число1"))
        num2=int(input("введите число2"))
        if operation=="+":
            print(summa(num1,num2))
        if operation=="-":
            print(minus(num1,num2))
        if operation=="*":
            print(umnosh(num1,num2))
        if operation=="/":
            print(delit(num1,num2))
    if tip_calculator == "калькулятор фигур":
        figure=str(input(" Circle, Rectangle, Triangle"))
        if figure=="Rectangle":
            side1=int(input("enter side1"))
            side2=int(input("enter side2"))
            print(Rectangle(side1,side2))
        if figure=="Circle":
            r=float(input("enter radius"))
            print( Circle(r))
        if figure=="Triangle":
            side1=int(input("enter side1"))
            side2 = int(input("enter side2"))
            print(Triangle(side1,side2))
