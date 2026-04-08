import flet as ft


def main(page : ft.Page):
    page.title = "Calculator App"
    page.window.height = 400
    page.window.width = 400

    btns = [['del', 'AC', '%', "/"],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', '.', '=']]
    
    buttons = []
    for row in btns:
        _row = []
        for btn in row:
            _row.append(ft.Button(
                content=btn,
                style=ft.ButtonStyle(

                )
            ))
        buttons.append(ft.Row(_row))
    
    my_stack = ft.Stack([ft.Column(buttons)])

    page.add(my_stack)
    



ft.run(main)