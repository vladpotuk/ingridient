import flet as ft
tf_user = ft.TextField(label="Введіть 5 інгрідієнтів,  з яких  ви хочете готувати??", width=200, height=200, multiline=True, max_lines=8, min_lines=8, border_radius = 25)
text_gpt = ft.TextField(label="З цього можна:", bgcolor="#DFC2B2", multiline=True, max_lines=100, min_lines=15,border_radius=25, width=1300, height=200)
def create_row_1():
    container = ft.Container(
        width=300,

        height=300,
        content=tf_user,
        padding=ft.Padding(20, 20, 20, 20),
    )
    card = ft.Card(
        elevation=10,
        color="#deb69d",
        width=1300,
        height=300,
        content=container,
    )
    return ft.Row([
        card
    ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
def create_row_3():
    return ft.Row([
        text_gpt
    ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
def main(page: ft.Page):
    page.title = "FletGpt"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#cab7b3"
    page.window_maximized = True

    r1 = create_row_1()

    def click_button(e):
        from gpt_core import send_request

        text_gpt.value = send_request(tf_user.value)
        text_gpt.update()
        page.update()

    bt = ft.ElevatedButton(text="Знайти", color="#677C77", width=300, height=50, elevation=10, on_click=click_button,)
    row = ft.Row([
        bt,
    ],
        alignment=ft.MainAxisAlignment.END,
    )
    container = ft.Container(
        height=140,
        padding=ft.Padding(0, 0, 50, 0),
        content=row,

    )
    r3 = create_row_3()
    column = ft.Column([
        r1,
        container,
        r3,
    ],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    page.add(column)
ft.app(target=main)