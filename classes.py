import math
import random

class Btn:
    def __init__(self, value, inv_value=None):
        self.org_value = value
        if not inv_value: # inverse symbol
            self.inv_value = value + "\u207B\u00B9"
        else:
            self.inv_value = inv_value

        self.value = value
    
    def toggle(self):
        if self.value == self.org_value:
            self.value = self.inv_value
        elif self.value == self.inv_value:
            self.value = self.org_value


class Calculator:
    def __init__(self):
        self.query = "0"
        self.__standard = [['\u232B', 'AC', '%', "/"],
                        ['7', '8', '9', '*'],
                        ['4', '5', '6', '-'],
                        ['1', '2', '3', '+'],
                        ['+/-', '0', '.', '=']]
        
        self.__extended = [['(', ')', 'mc', 'm+', 'm-', 'mr'],
                        ['2\u207F\u1D48', 'x\u00B2', 'x\u00B3', 'x\u02B8', Btn('e\u02E3', 'y\u02E3'), Btn('10\u02E3', '2\u02E3')],
                        ['x\u207B\u00B9', '\u221Ax', '\u221Bx', '\u207F\u221Ax', Btn('ln', 'log\u1D67'), Btn('log', 'log\u2082')],
                        ['x!', Btn('sin'), Btn('cos'), Btn('tan'), 'e', 'EE'],
                        ['Rand', Btn('sinh'), Btn('cosh'), Btn('tanh'), '\u03C0', 'Rad']]
    
    @property
    def standard(self) -> list:
        return self.__standard

    @property
    def extended(self) -> list: # Done
        arr = [[0 for i in range(6)] for j in range(5)]
        for i in range(5):
            for j in range(6):
                if type(self.__extended[i][j]) == str:
                    arr[i][j] = self.__extended[i][j]
                else:
                    arr[i][j] = self.__extended[i][j].value
        
        return arr
    
    @property
    def query(self) -> str:
        return self.query
    
    # This function handles the query in mathematical language
    def add_query(self, expr : str):
        symbols = ['+', '-', '*', '/', '%']
        powers = {'\u00B2': '**2', '\u00B3': '**3', '\u207B\u00B9': '**(-1)', '\u02B8': '**'}
        roots = {'\u221A': '**(1/2)', '\u221B': '**(1/3)', '\u207F\u221A': '**(1/y)'}

        # Standard buttons
        if expr.isdigit() or expr in (".", ')'): # numbers 0-9 or decimal point or closing bracket
            self.query += expr
        elif expr in symbols:
            if self.query[-1] in symbols: # consecutive symbols not allowed
                self.query = self[:-1] + expr
            else: # not consecutive symbols
                self.query += expr

        elif expr == "AC":
            self.query = "0"
        elif expr == "\u232B": # delete btn
            if len(self.query) == 1:
                self.query = "0"
            else:
                self.query = self.query[:-1]
        elif expr == "+/-":
            if self.query[0] == '-':
                self.query = self.query[1:]
            else:
                self.query = '-' + self.query
        elif expr == "=":
            self.query = "0"

        # Extended buttons
        elif expr == '(':
            if self.query[-1] in symbols:
                self.query += '('
            else:
                self.query += '*('
        # Let's skip mc, m+, m-, mr
        elif expr[0] == 'x':
            # x^2, x^3, x^y, x^-1, x!
            if expr == "x!":
                self.query = 'math.factorial(' + self.query + ')'
            else:
                self.query += powers[expr[1:]]
        elif expr in ["sin", 'cos', 'tan', 'sinh', 'cosh', 'tanh']: # trigo
            self.query = f'math.{expr}(' + self.query + ')'
        elif expr in [x+"\u207B\u00B9" for x in ["sin", 'cos', 'tan', 'sinh', 'cosh', 'tanh']]: # inv trigo
            self.query = f'math.a{expr[:-2]}(' + self.query + ')'
        elif expr == 'ln':
            self.query = 'math.log(' + self.query + ')'
        elif expr == 'log':
            self.query = 'math.log10(' + self.query + ')'
        elif expr == 'log\u2082': # log base 2
            self.query = 'math.log2(' + self.query + ')'
        elif expr == 'log\u1D67': # log base y
            pass # TODO
        elif expr[-1] == 'x': # sqrt x, cbrt x, y-th root
            self.query += roots[expr[:-1]]
        elif expr == 'Rand':
            self.query += f'{random.random()}'
        elif expr[-1] == '\u02E3': # power x
            # 2^x, 10^x, e^x, y^x
            if expr[:-1] in ('2', '10'):
                self.query = expr[:-1] + '**' + '(' + self.query + ')'
            elif expr[:-1] == 'e':
                self.query = 'math.e**' + '(' + self.query + ')'
            elif expr[:-1] == 'y':
                pass # TODO y^x
        elif expr == 'e':
            if self.query[-1] in symbols:
                self.query += 'math.e'
            else:
                self.query += '*math.e'
        elif expr == '\u03C0': # pi
            if self.query[-1] in symbols:
                self.query += 'math.pi'
            else:
                self.query += '*math.pi'
        elif expr == 'EE':
            pass
        elif expr in ('Rad', 'Deg'):
            pass # TODO
            
        
        else: # for other buttons don't do anything
            pass

        
            



    
    def __str__(self):
        txt = ""
        for i in range(5):
            for j in range(6):
                txt += self.extended[i][j] + " "
            txt += '\n'
        
        return txt

    def toggle(self) -> bool:
        # the user clicked on "2nd" button
        for i in range(5):
            for j in range(6):
                if type(self.__extended[i][j]) == Btn:
                    self.__extended[i][j].toggle()

        
        return True
    
    def str_to_math(self, expr : str):
        symbols = ['+', '-', '*', '/', '%']
        if expr.isdigit():
            pass
        elif expr in symbols:
            pass
    
    def calculate(self):
        pass

calc = Calculator()