# -*- coding: utf-8 -*-
class WrongArithmeticalExpression(Exception):
    pass


class NonBalancedParenthesis(Exception):
    pass


class Operator(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value

    @property
    def is_opening_parenthesis(self):
        if self.value in '(':
            return True
        else:
            return False

    @property
    def is_closing_parenthesis(self):
        if self.value in ')':
            return True
        else:
            return False

    @property
    def is_parenthesis(self):
        return self.is_closing_parenthesis or self.is_opening_parenthesis

    @property
    def is_operator(self):
        if self.value in u'+-/*':
            return True
        else:
            return False

    @property
    def is_numeric(self):
        return self.value.isnumeric()

    def is_valid_pair_with(self, next_op):
        valid_pairs = [lambda l_op, r_op: (l_op.is_opening_parenthesis, r_op.is_numeric),
                       lambda l_op, r_op: (l_op.is_numeric, r_op.is_operator),
                       lambda l_op, r_op: (l_op.is_operator, r_op.is_numeric),
                       lambda l_op, r_op: (l_op.is_closing_parenthesis, r_op.is_closing_parenthesis),
                       lambda l_op, r_op: (l_op.is_opening_parenthesis, r_op.is_opening_parenthesis),
                       lambda l_op, r_op: (l_op.is_numeric, r_op.is_closing_parenthesis),
                       lambda l_op, r_op: (l_op.is_operator, r_op.is_opening_parenthesis),
                       lambda l_op, r_op: (l_op.is_closing_parenthesis, r_op.is_operator)]
        for x in valid_pairs:
            if x(self, next_op) == (True, True):
                return True
        raise WrongArithmeticalExpression(u'Неправильное сочетание операторов \'{}{}\''.format(self, next_op))


class ArithmeticalExpression(object):
    @classmethod
    def transform_to_postfix(cls, expression):
        op_stack = []
        result_stack = []
        op_priority = {u"*": 3,
                       u"/": 3,
                       u"+": 2,
                       u"-": 2,
                       u"(": 1}
        for op in expression.operator_list:
            if op.is_numeric:
                result_stack.append(op)
            elif op.is_opening_parenthesis:
                op_stack.append(op)
            elif op.is_closing_parenthesis:
                top_token = op_stack.pop()
                while not top_token.is_opening_parenthesis:
                    result_stack.append(top_token)
                    top_token = op_stack.pop()
            else:
                while not len(op_stack) == 0 and (op_priority[op_stack[-1].value] >= op_priority[op.value]):
                    result_stack.append(op_stack.pop())
                op_stack.append(op)
        while not len(op_stack) == 0:
            result_stack.append(op_stack.pop())
        expression.postfix_operator_list = result_stack

    def __init__(self, string_exp):
        self.string_exp = string_exp
        self._operator_list = None
        self.postfix_operator_list = None

    def __repr__(self):
        return ' '.join(op.value for op in self.operator_list)

    def calculate(self):
        def do_math(token, operand1, operand2):
            if token == '-':
                return operand1.__sub__(operand2)
            if token == '+':
                return operand1.__add__(operand2)
            if token == '*':
                return operand1.__mul__(operand2)
            if token == '/':
                try:
                    return operand1.__truediv__(operand2)
                except ZeroDivisionError as exc:
                    raise WrongArithmeticalExpression('Делить на ноль нельзя')

        op_stack = []
        for op in self.postfix_operator_list:
            if op.is_numeric:
                op_stack.append(int(op.value))
            else:
                operand2 = op_stack.pop()
                operand1 = op_stack.pop()
                result = do_math(op.value, operand1, operand2)
                op_stack.append(result)
        return op_stack.pop()

    def parse_string_exp(self):
        result = []
        number = ''
        for symbol in self.string_exp:
            if symbol in u'()+-/*':
                if number:
                    result.append(number)
                    number = ''
                result.append(symbol)
            else:
                if symbol.isdigit():
                    number += symbol
                else:
                    raise WrongArithmeticalExpression('Можно вводить только цифры и знаки арифметических операций!')
        if number:
            result.append(number)
        return [Operator(op_value) for op_value in result]

    def check_syntax(self):
        operator_count = 0
        if len(self.operator_list) < 3:
            raise WrongArithmeticalExpression('Должно быть минимум три оператора')

        previous_op = self.operator_list[0]
        for op in self.operator_list[1:]:
            if previous_op.is_operator:
                operator_count += 1
            previous_op.is_valid_pair_with(op)
            previous_op = op

        last_op = self.operator_list[-1]
        if not (last_op.is_closing_parenthesis or last_op.is_numeric):
            raise WrongArithmeticalExpression('Последним оператором должны быть закрывающие скобки или число')

        if operator_count == 0:
            raise WrongArithmeticalExpression('В выражении должен быть хотя бы один оператор')

    def check_parenthesis(self):
        paren_stack = []
        for op in [op for op in self.operator_list if op.is_parenthesis]:
            if op.is_opening_parenthesis:
                paren_stack.append(op)
            elif op.is_closing_parenthesis and paren_stack:
                paren_stack.pop()
            else:
                raise NonBalancedParenthesis('Лишняя закрывающая скобка')
        if paren_stack:
            raise NonBalancedParenthesis('Лишняя открывающая скобка')

    @property
    def operator_list(self):
        self._operator_list = self.parse_string_exp()
        return self._operator_list
