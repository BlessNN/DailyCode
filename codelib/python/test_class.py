#coding=utf-8
class Employee:
    '''
    For help info
    '''
    classspec = "testing class"

    def __init__(self, name, pay):
        self.com = "Baidu"
        self.name = name
        self.pay = pay
#    @instancemethod 不需要写注明
    def say(self):
        '''
        For help(say) info 
        '''
        print self.com + ":" + self.name +" said something(an instance)"
    @classmethod
    def clsSay(cls):
        print cls.classspec+" said something(a class)"
    @staticmethod        #Just a function
    def stcSay():
        print classspec  # NoWay   
        print self.name  # NoWay
e = Employee('Mike',10000)
e.say()

