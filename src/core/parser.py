import typing

MATH_SYMBOL = [
    '+',
    '-',
    '*',
    '/',
    '×',
    ':'
]


class Parser:

    def __init__(
        self,
        expression: str
    ):
        self.expression: str = expression.replace(" ", "")
        self.answer: typing.Union[str, int] = 0
        
        #METADATA
        self.symbol: list = []

        self.symbol_splitter()

    def is_equation(self):
        return '=' in self.symbol

    def symbol_splitter(self):
        sym = ""
        for i, char in enumerate(self.expression):
            if i == len(self.expression)-1:
                self.symbol.append(sym+char)
            if char.isdigit():
                sym += char
            else:
                if char in MATH_SYMBOL:
                    self.symbol.append(sym)
                    self.symbol.append(char)
                    sym = ""

        if not self.is_equation():
            self.evaluate()

    def evaluate(self):
        while len(self.symbol) != 1:
            print(self.symbol)
            for i, symbol in enumerate(self.symbol):
                if symbol in MATH_SYMBOL:
                    OP1 = self.symbol[i-1]
                    OP2 = self.symbol[i+1]

                    if symbol == '+':
                        self.answer = int(OP1) + int(OP2)

                    del self.symbol[i-1:i+2]

                    self.symbol.insert(0, self.answer)
                    break

