"""
8)Dollar
Create function dollarize() that takes Float and returns dollarized format:
dollarize(123456.78901) -> "$123,456.80"
dollarize(-123456.7801) -> "-$123,456.78"
dollarize(1000000) -> "$1,000,000"
Convert this function into useful class MoneyFmt. MoneyFmt contains single data value(the
amount) and 4 methods.
"init" //constructor initializes the data value
"update" //method replaces data value with new one
"repr" //methods returns Float value
"str" //method, that implements logic of dollarize() method
//The output will look like this:
import moneyfmt
cash = moneyfmt.MoneyFmt(12345678.021)
print(cash) -- returns "$12,345,678.02"
cash.update(100000.4567)
print(cash) -- returns "$100,000.46"
cash.update(-0.3)
print(cash) -- returns "-$0.30"
repr(cash) -- returns -0.3
"""

class MoneyFmt():
    def __init__(self, amount):
        self.amount = amount
    
    def __str__(self):
        return "${:,.2f}".format(self.amount)

    def update(self, amount):
        self.amount = amount
        # print('Введите число для дальнейшего форматирования:')
        # self.amount = int(input("==>"))
    
    def repr(self):
        print(f"Преобразование в целое число с плавающей точкой {float(self.amount)}")

    def str_(self):
        print(f"Преобразование в строчный тип данных {str(self.amount)}")


