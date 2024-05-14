import flet as ft

def main(page: ft.page):
    page.title = "calculator"
    page.window_height = 400
    page.window_width = 350
    page.bgcolor = "#232323"

    def keyboard(e):
        data = e.control.data
        if data in ("1","2","3","4","5","6","7","8","9","0",".","+","-","*","/","(",")"):
            txt.value = str(txt.value) + str(data)
            page.update()
        if data == "=":
            try:
                txt.value = str(eval(txt.value))
                page.update()
            except ZeroDivisionError:
                txt.value=("division by zero")
                page.update()
        if data=="e":
            st = list(txt.value)
            st.pop()
            txt.value="".join(map(str,st))
            page.update()
        if data=="C":
            txt.value = ""
            page.update()


    txt = ft.TextField(
        read_only=True,
        border_color="white",
        text_style=ft.TextStyle(size=30,color="white")
    )
    page.add(txt)
    btn_e = ft.ElevatedButton(
        text="<",bgcolor="#FFFFFF",color="#232323",data="e",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_po = ft.ElevatedButton(
        text="(",bgcolor="#FFFFFF",color="#232323",data="(",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_pc = ft.ElevatedButton(
        text=")",bgcolor="#FFFFFF",color="#232323",data=")",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_dv = ft.ElevatedButton(
        text="/",bgcolor="#FFFFFF",color="#232323",data="/",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )


    r1= ft.Row(
        controls=[btn_e,btn_po,btn_pc,btn_dv],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    btn_7 = ft.ElevatedButton(
        text="7", bgcolor="#FFFFFF", color="#232323",data="7",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_8 = ft.ElevatedButton(
        text="8", bgcolor="#FFFFFF", color="#232323",data="8",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_9 = ft.ElevatedButton(
        text="9", bgcolor="#FFFFFF", color="#232323",data="9",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_ml = ft.ElevatedButton(
        text="*", bgcolor="#FFFFFF", color="#232323",data="*",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r2 = ft.Row(
        controls=[btn_7, btn_8, btn_9, btn_ml],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )


    btn_4 = ft.ElevatedButton(
        text="4", bgcolor="#FFFFFF", color="#232323",data="4",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_5 = ft.ElevatedButton(
        text="5", bgcolor="#FFFFFF", color="#232323",data="5",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_6 = ft.ElevatedButton(
        text="6", bgcolor="#FFFFFF", color="#232323",data="6",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_sub = ft.ElevatedButton(
        text="-", bgcolor="#FFFFFF", color="#232323",data="-",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r3 = ft.Row(
        controls=[btn_4, btn_5, btn_6, btn_sub],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )


    btn_1 = ft.ElevatedButton(
        text="1", bgcolor="#FFFFFF", color="#232323",data="1",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_2 = ft.ElevatedButton(
        text="2", bgcolor="#FFFFFF", color="#232323",data="2",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_3 = ft.ElevatedButton(
        text="3", bgcolor="#FFFFFF", color="#232323",data="3",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_sm = ft.ElevatedButton(
        text="+", bgcolor="#FFFFFF", color="#232323",data="+",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r4 = ft.Row(
        controls=[btn_1, btn_2, btn_3, btn_sm],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )


    btn_C = ft.ElevatedButton(
        text="C", bgcolor="#FFFFFF", color="#232323",data="C",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_0 = ft.ElevatedButton(
        text="0", bgcolor="#FFFFFF", color="#232323",data="0",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_dot = ft.ElevatedButton(
        text=".", bgcolor="#FFFFFF", color="#232323",data=".",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )
    btn_eq = ft.ElevatedButton(
        text="=", bgcolor="#FFFFFF", color="#232323",data="=",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
    )

    r5 = ft.Row(
        controls=[btn_C, btn_0, btn_dot, btn_eq],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    page.add(r1,r2,r3,r4,r5)



ft.app(target=main)


