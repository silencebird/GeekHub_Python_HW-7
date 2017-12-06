
class Calc(object):
    file = open('./expressions.txt', 'a+')

    def sum(self, *args):
        sum = 0
        i = 0
        expression = ""
        for i in args:
            sum += i
            if args[-1] != i:
                expression += str(i) + '+'
            else:
                expression += str(i)

        expression += '=' + str(sum)+ '\n'
        Calc.file.write(expression)

    def devision(self, *args):
        devision = 0
        i = 0
        expression = ""
        for i in args:
            devision -= i
            if args[-1] != i:
                expression += str(i) + '-'
            else:
                expression += str(i)

        expression += '=' + str(devision)+ '\n'
        Calc.file.write(expression)

    def multiplication(self, *args):
        multiplication = 0
        i = 0
        expression = ""
        for i in args:
            multiplication *= i
            if args[-1] != i:
                expression += str(i) + '*'
            else:
                expression += str(i)

        expression += '=' + str(multiplication)+ '\n'
        Calc.file.write(expression)

    def ratio(self, *args):
        ratio = 0
        i = 0
        expression = ""
        for i in args:
            ratio /= i
            if args[-1] != i:
                expression += i + '/'
            else:
                expression += i

                expression += '=' + ratio + '\n'
        Calc.file.write(expression)

    @staticmethod
    def last_result():
        Calc.file.seek(0)
        left = (Calc.file.read().rfind("=")+1)
        Calc.file.seek(0)
        right = (len(Calc.file.read()))
        Calc.file.seek(0)
        last = Calc.file.read()[left:right]
        return last

    @staticmethod
    def close_file():
        Calc.file.close()

calc = Calc()



calc.sum(1, 2)
calc.sum(3, 4, 5)
calc.sum(6, 7)
calc.sum(8, 9)

print(Calc.last_result())

Calc.close_file()
