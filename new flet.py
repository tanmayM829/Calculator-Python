import flet as ft
from classes import Calculator

## Global Variables
calc = Calculator()
STACK = None
MEMORY = {
    "memory": None,
    "ntype": 'deg' # can be rand/deg
}

def calculate(val : str):
    res = STACK.controls[0].controls[0].content.value
    symbols = ['+', '-', '*', '/', '%', '.', '(', ')']

    if val.isdigit() or val in symbols: # numbers or symbols
        if res in ('0', 'Error'):
            res = val
        elif res[-1] in symbols[:5] and val in symbols[:5]: # to prevent double symbols
            res = res[:-1] + val
        elif val == '(':
            if res[-1] in symbols[:5]: # there's a symbol
                res += '('
            else:
                res += '*('
        else:
            res += val

    elif val == '=':
        try:
            if res[-1] == '%': res = res[:-1] + '/100'
            res = str(eval(res))

        except: res = "Error"
    elif val == '\u232B': # delete btn
        if len(res) == 1: res = "0"
        else: res = res[:-1]

    elif val == 'AC':
        res = "0"
    elif val == '+/-':
        res = '-' + res if res[0] != '-' else res[1:]

    # Extended Buttons
    memory_btns = ['mc', 'm+', 'm-', 'mr']
    trigo_funcs = ['sin', 'cos', 'tan', 'sinh', 'cosh', 'tanh']
    all_trig_funcs = trigo_funcs + [x+"\u207B\u00B9" for x in trigo_funcs] # \u207B\u00B9 is power -1

    if val in all_trig_funcs:
        pass
    
    STACK.controls[0].controls[0].content.value = res


def make_flet_btns(btns : list, btype : str | None = "standard") -> list:
    style_info = {
        "standard": {
            "bg": lambda i, j: ft.Colors.ORANGE if j == 3 else ft.Colors.BLUE_GREY_100 if i == 0 else None,
            "color": lambda i, j: ft.Colors.BLACK if j==3 or i==0 else ft.Colors.WHITE
        },
        "extended": {
            "bg": lambda i, j: ft.Colors.with_opacity(0.2, ft.Colors.BLACK_45),
            "color": lambda i, j: ft.Colors.WHITE
        }
    }

    buttons = []
    for i in range(len(btns)):
        row = []
        for j in range(len(btns[i])):
            row.append(ft.Button(
                content=ft.Text(btns[i][j], size=18),
                style=ft.ButtonStyle(
                    shape=ft.StadiumBorder(),
                    padding=10,
                    bgcolor = style_info[btype]["bg"](i, j),
                    color = style_info[btype]["color"](i, j)
                ),
                width=80,
                height=40,
                on_click=lambda e, v=btns[i][j]: calculate(v)
            ))
        buttons.append(ft.Row(row))

    return buttons

def main(page : ft.Page):
    page.title = "Calculator App"
    page.window.height = 400
    page.window.width = 950
    page.bgcolor = ""

    global STACK
    
    res_field = ft.Container(
        content=ft.Text(
            value=calc.query,
            align=ft.Alignment.CENTER_RIGHT,
            color=ft.Colors.BLACK,
            size=24,
            margin=10
        ),
        height=50,
        bgcolor="#e8e8e8",
        border_radius=16
    )


    buttons = make_flet_btns(calc.standard)
    extended_buttons = make_flet_btns(calc.extended, btype="extended")
    
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

    STACK = my_stack
    

if __name__ == "__main__":
    ft.run(main)