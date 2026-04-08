import flet as ft

STACK = None

def calc(val : str):
    res = STACK.controls[0].controls[0].content.value
    symbols = ['+', '-', '*', '/', '%', '.']

    if val.isdigit() or val in symbols:
        if res in ('0', 'Error'):
            res = val
        elif res[-1] in symbols and val in symbols:
            res = res[:-1] + val
        else:
            res += val

    elif val == '=':
        try:
            if res[-1] == '%': res = res[:-1] + '/100'
            res = str(eval(res))

        except: res = "Error"
    elif val == '\u232B':
        if len(res) == 1: res = "0"
        else: res = res[:-1]

    elif val == 'AC':
        res = "0"
    elif val == '+/-':
        res = '-' + res if res[0] != '-' else res[1:]

    
    STACK.controls[0].controls[0].content.value = res


def make_flet_btns(btns : list, btype : str | None = "standard") -> list:
    buttons = []
    for i in range(len(btns)):
        row = []
        for j in range(len(btns[i])):
            if btype == "standard":
                if j == len(btns[i])-1: bg = ft.Colors.ORANGE
                elif i == 0: bg = ft.Colors.BLUE_GREY_100
                else: bg = None

            elif btype == "extended":
                bg = ft.Colors.with_opacity(0.2, ft.Colors.BLUE)

            row.append(ft.Button(
                content=ft.Text(btns[i][j], size=18),
                style=ft.ButtonStyle(
                    shape=ft.StadiumBorder(),
                    padding=10,
                    bgcolor = bg,
                    color = ft.Colors.BLACK if j == len(btns[i])-1 or i == 0 else ft.Colors.GREY_100
                ),
                width=80,
                height=40,
                on_click=lambda e, v=btns[i][j]: calc(v)
            ))
        buttons.append(ft.Row(row))

    return buttons

def main(page : ft.Page):
    page.title = "Calculator App"
    page.window.height = 400
    page.window.width = 1000
    page.bgcolor = ""

    btns = [['\u232B', 'AC', '%', "/"],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['+/-', '0', '.', '=']]
    
    extra_btns = [['(', ')', 'mc', 'm+', 'm-', 'mr'],
                  ['2\u207F\u1D48', 'x\u00B2', 'x\u00B3', 'A', 'B', 'C'],
                  ['a', 'b', 'c', 'd', 'e', 'f'],
                  ['a', 'b', 'c', 'd', 'e', 'f'],
                  ['a', 'b', 'c', 'd', 'e', 'f']]
    

    
    res_field = ft.Container(
        content=ft.Text(
            value="0",
            align=ft.Alignment.CENTER_RIGHT,
            color=ft.Colors.BLACK,
            size=24,
            margin=10
        ),
        height=50,
        bgcolor="#e8e8e8",
        border_radius=16
    )


    buttons = make_flet_btns(btns)
    extended_buttons = make_flet_btns(extra_btns, btype="extended")
    
    standard_btns = ft.Container(
        content=ft.Column(buttons),
        bgcolor="#525352",
        border_radius=16,
        padding=10
    )

    extended_btns = ft.Container(
        content=ft.Column(extended_buttons),
        bgcolor="#8F8F8F",
        border_radius=16,
        padding=10
    )
    
    my_stack = ft.Stack([
        ft.Column(controls=[
            res_field,
            ft.Row([extended_btns, standard_btns])
        ])
    ], expand=True)

    page.add(my_stack)

    global STACK
    STACK = my_stack
    

if __name__ == "__main__":
    ft.run(main)