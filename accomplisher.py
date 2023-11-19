import math

class Accomplisher:
    def __init__(self, ast):
        self.ast = ast
        self.binary_operations = {
            '+': lambda a, b: ('number', a[1] + b[1]),
            '-': lambda a, b: ('number', a[1] - b[1]),
            '^': lambda a, b: ('number', a[1] ** b[1]),
            '**': lambda a, b: ('number', a[1] ** b[1]),
            '*': lambda a, b: ('number', a[1] * b[1]),
            '/': lambda a, b: ('number', a[1] / b[1]),
        }

        self.unary_operations = {
            '+': lambda a: ('number', a[1]),
            '-': lambda a: ('number', -a[1]),
            'cos': lambda a: ('number', math.cos(a[1])),
            'sin': lambda a: ('number', math.sin(a[1]))
        }

    def accomplish(self):
        return self.__accomplish(self.ast)

    def __accomplish(self, operation):
        if operation is None:
            return ('none', None)

        operation_type = operation[0];

        if operation_type == 'grouped':
            return self.__accomplish(operation[1]);

        elif operation_type == 'number':
            return operation

        elif operation_type == 'unary':
            operator = operation[1]

            if operator in self.unary_operations:
                return self.unary_operations[operator](self.__accomplish(operation[2]))
            else:
                raise RuntimeError(f'Invalid operator {operator}')

        elif operation_type == 'binop':
            operator = operation[1]

            if operator in self.binary_operations:
                return self.binary_operations[operator](self.__accomplish(operation[2]), self.__accomplish(operation[3]))
            else:
                raise RuntimeError(f'Invalid operator{operator}')

        else:
            raise RuntimeError(f'Invalid opetration{operation_type}')
 
