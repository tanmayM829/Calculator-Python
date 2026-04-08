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
        self.query = None
        self.__standard = [['\u232B', 'AC', '%', "/"],
                        ['7', '8', '9', '*'],
                        ['4', '5', '6', '-'],
                        ['1', '2', '3', '+'],
                        ['+/-', '0', '.', '=']]
        
        self.__extended = [['(', ')', 'mc', 'm+', 'm-', 'mr'],
                        ['2\u207F\u1D48', 'x\u00B2', 'x\u00B3', 'x\u02B8', Btn('e\u02E3', 'y\u02E3'), Btn('10\u02E3', '2\u02E3')],
                        ['x\u207B\u00B9', '\u221Ax', '\u221Bx', '\u207F\u221Ax', Btn('ln', 'log\u1D67'), Btn('log', 'log\u2082')],
                        ['x!', Btn('sin'), Btn('cos'), Btn('tan'), '\U0001D452', 'EE'],
                        ['Rand', Btn('sinh'), Btn('cosh'), Btn('tanh'), '\u03C0', 'Rad']]
    
    @property
    def standard(self):
        return self.__standard

    @property
    def extended(self):
        arr = [[0 for i in range(6)] for j in range(5)]
        for i in range(5):
            for j in range(6):
                if type(self.__extended[i][j]) == str:
                    arr[i][j] = self.__extended[i][j]
                else:
                    arr[i][j] = self.__extended[i][j].value
        
        return arr
    
    def __str__(self):
        txt = ""
        for i in range(5):
            for j in range(6):
                txt += self.extended[i][j] + " "
            txt += '\n'
        
        return txt

    def toggle(self):
        # the user clicked on "2nd" button
        for i in range(5):
            for j in range(6):
                if type(self.__extended[i][j]) == Btn:
                    self.__extended[i][j].toggle()

        
        print(self)


    


# A Global Variable
x = Calculator() # a calculator object is made

x.toggle()
x.toggle()
x.toggle()