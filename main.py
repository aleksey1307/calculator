import flet as ft
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

def main(page):
    def btn_click(e):
        if not txt_name1.value:
            txt_name1.error_text = "Please enter side1"
            page.update()
        else:
            name = txt_name1.value
            page.add(ft.Text(name))
        if not txt_name2.value:
            txt_name1.error_text = "Please enter side1"
            page.update()
        else:
            name = txt_name2.value
            page.add(ft.Text(name))


    txt_name1 = ft.TextField(label="Your side1")
    txt_name2 = ft.TextField(label="Your side2")

    page.add(txt_name1, ft.ElevatedButton("side1", on_click=btn_click))
    page.add(txt_name1, ft.ElevatedButton("side2", on_click=btn_click))


ft.app(target=main)


    while True:
        tip_calculator = str(input("введите калькулятор чисел или калькулятор фигур или стоп"))
        if tip_calculator=="калькулятор чисел":
            operation=str(input("+, -, *, /"))
            num1=int(input("введите число1"))
            num2=int(input("введите число2"))
            if operation=="+":
                print(summa(num1,num2))
            elif operation=="-":
                print(minus(num1,num2))
            elif operation=="*":
                print(umnosh(num1,num2))
            elif operation=="/":
                print(delit(num1,num2))
        elif tip_calculator == "калькулятор фигур":
            figure=str(input(" Circle, Rectangle, Triangle"))
            if figure=="Rectangle":
                side1=int(input("enter side1"))
                side2=int(input("enter side2"))
                print(Rectangle(side1,side2))
            elif figure=="Circle":
                r=float(input("enter radius"))
                print( Circle(r))
            elif figure=="Triangle":
                side1=int(input("enter side1"))
                side2 = int(input("enter side2"))
                print(Triangle(side1,side2))
        elif tip_calculator == "стоп":
            break





    ft.app(target=main)