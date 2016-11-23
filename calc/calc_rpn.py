# !/usr/bin/python

class Calculator(object):
    def __init__(self):
        pass

    def calc(self, s):
        rpn = self.infix_to_rpn(s)
        print rpn
        return self.calc_rpn(rpn)

    def op_cmp (self, op1, op2):
        if op1 == '*' or op1 == '/':
            return 1
        if (op1 == '+' or op1 == '-') and (op2 == '+' or op2 == '-'):
            return 1

        return -1

    def infix_to_rpn(self, s):
        out = [] # used as a list
        op = [] # used as a stack
        for c in s:
            if self.isDigit(c):
                out.append(c)
            elif self.isOp(c):
                out.append(' ')
                if len(op) == 0:
                    op.append(c)
                elif op[-1] == '(':
                    op.append(c)
                elif self.op_cmp(op[-1], c) >= 0:
                    out.append(op.pop())
                    op.append(c)
                else:
                    op.append(c)
            elif self.isLeftParenthese(c):
                op.append(c)
            elif self.isRightParenthese(c):
                p = op.pop()
                while (not self.isLeftParenthese(p)):
                    out.append(p)
                    p = op.pop()

        while len(op) != 0:
            out.append(op.pop())
        return out



    def isDigit(self, c):
        return c >= '0' and c <= '9'

    def isOp(self, c):
        return c == '+' or c == '-' or c == '*' or c == '/'

    def isLeftParenthese(self, c):
        return c == '('

    def isRightParenthese(self, c):
        return c == ')'

    def calc_rpn(self, s):
        nums = []
        ops = []
        i = 0
        while i < len(s):
            c = s[i]
            if self.isDigit(c):
                num = 0
                while (self.isDigit(c)):
                    num = num*10 + (ord(c)-ord('0'))
                    i += 1
                    c = s[i]
                nums.append(num)
            if self.isOp(c):
                if c == '+':
                    num2 = nums.pop()
                    num1 = nums.pop()
                    nums.append(num1 + num2)
                elif c == '-':
                    num2 = nums.pop()
                    num1 = nums.pop()
                    nums.append(num1 - num2)
                elif c == '*':
                    num2 = nums.pop()
                    num1 = nums.pop()
                    nums.append(num1 * num2)
                elif c == '/':
                    num2 = nums.pop()
                    num1 = nums.pop()
                    nums.append(num1 / num2)

            i += 1



        return nums[0]


calc = Calculator()

s = raw_input()

print calc.calc(s)
