'''
    unittest:单元测试框架

    1.子类继承TestCase
    2.写测试用例:testXxxxx
    任务1：
        使用邮件发送测试报告
        温馨提示：用户名，密码（smtp授权码开通即可。）
    任务2：执行减法，乘法，除法，测试用例。并生成测试报告。
'''
from Calc import Calc
from unittest import TestCase

class TestCalc(TestCase):

    def testAdd1(self):
        #
        a = 6
        b = 5
        s = 10

        calc = Calc()
        sum = calc.add(a,b)

        self.assertEqual(s,sum)


    def testAdd2(self):
        #
        a = -6
        b = -5
        s = -11

        calc = Calc()
        sum = calc.add(a,b)

        self.assertEqual(s,sum)


    def testAdd3(self):
        #
        a = -6
        b = 5
        s = -1

        calc = Calc()
        sum = calc.add(a,b)

        self.assertEqual(s,sum)



    def testAdd4(self):
        #
        a = 6
        b = -5
        s = 1

        calc = Calc()
        sum = calc.add(a,b)

        self.assertEqual(s,sum)


class TestMinus(TestCase):

    def testAdd1(self):
        a = 5
        b = 6
        s = -1

        calc = Calc()
        num = calc.minus(a, b)

        self.assertEqual(s, num)

    def testAdd2(self):
        a = -5
        b = 6
        s = -11

        calc = Calc()
        num = calc.minus(a, b)

        self.assertEqual(s, num)

    def testAdd3(self):
        a = -5
        b = -6
        s = 1

        calc = Calc()
        num = calc.minus(a,b)
        self.assertEqual(s,num)

    def testAdd4(self):
        a = 5
        b = -6
        s = 11

        calc = Calc()
        num = calc.minus(a,b)
        self.assertEqual(s,num)

class Testmulti(TestCase):

    def testAdd1(self):
        a = 5
        b = 6
        s = 30

        calc = Calc()
        num = calc.multi(a, b)

        self.assertEqual(s, num)

    def testAdd2(self):
        a = -5
        b = 6
        s = 20

        calc = Calc()
        num = calc.multi(a, b)

        self.assertEqual(s, num)

    def testAdd3(self):
        a = -5
        b = -6
        s = -30

        calc = Calc()
        num = calc.multi(a,b)
        self.assertEqual(s,num)

    def testAdd4(self):
        a = 5
        b = -6
        s = -30

        calc = Calc()
        num = calc.multi(a,b)
        self.assertEqual(s,num)

class Testdeivsion(TestCase):

    def testAdd1(self):
        a = 5
        b = 6
        s = 0

        calc = Calc()
        num = calc.devision(a, b)

        self.assertEqual(s, num)

    def testAdd2(self):
        a = -5
        b = 10
        s = -0.5

        calc = Calc()
        num = calc.devision(a, b)

        self.assertEqual(s, num)

    def testAdd3(self):
        a = -10
        b = -5
        s = 2

        calc = Calc()
        num = calc.devision(a,b)
        self.assertEqual(s,num)

    def testAdd4(self):
        a = 10
        b = -5
        s = -2

        calc = Calc()
        num = calc.devision(a,b)






























