# !/usr/bin/python

class Calculator:
    def __init__(self):
        pass

    def calc(self, s):
        """
        :rtype int
        """
        nums = []
        ops = []
        cur = 0
        i = 0
        while i < len(s):
            c = s[i]
            if self.isDigit(c):
                num = 0
                while  i < len(s) and self.isDigit(c):
                    num = num*10+(ord(c)-ord('0'))
                    i += 1
                    if i >= len(s):
                        break
                    c = s[i]
                nums.append(num)

            if i >= len(s):
                break

            c = s[i]

            if self.isOp(c):
                if len(ops) == 0:
                    ops.append(c)
                elif self.op_cmp(ops[-1], c) >= 0:
                    while (len(ops) > 0 and self.op_cmp(ops[-1], c) >= 0):
                        nums.append(self.calc_single(ops.pop(), nums.pop(), nums.pop()))
                    ops.append(c)
                else:
                    ops.append(c)

            elif self.isLeftParenthese(c):
                ops.append(c)
            elif self.isRightParenthese(c):
                p = ops.pop()
                while (not self.isLeftParenthese(p)):
                    nums.append(self.calc_single(p, nums.pop(), nums.pop()))
                    p = ops.pop()
            i += 1


        while len(ops) != 0:
            nums.append(self.calc_single(ops.pop(), nums.pop(), nums.pop()))


        return nums[0]



    def calc_single(self, op, num2, num1):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 / num2

        return 0


    def op_cmp (self, op1, op2):
        if op1 == '*' or op1 == '/':
            return 1
        if (op1 == '+' or op1 == '-') and (op2 == '+' or op2 == '-'):
            return 1

        return -1


    def isDigit(self, c):
        return c >= '0' and c <= '9'

    def isOp(self, c):
        return c == '+' or c == '-' or c == '*' or c == '/'

    def isLeftParenthese(self, c):
        return c == '('

    def isRightParenthese(self, c):
        return c == ')'



calc = Calculator()

s = raw_input()

print calc.calc(s)
