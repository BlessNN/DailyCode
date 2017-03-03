#coding=utf-8
class Parent:
    parentAttr = "parent attr"
    def __init__(self):
        print "调用父类构造方法"
    def parentMed(self):
        print "调用父类方法"
    def setAttr(self,agr):
        Parent.parentAttr = agr
    def showAttr(self):
        print Parent.parentAttr

class Child(Parent):
    def __init__(self):
        # 默认先选用子类的方法，找不到再到父类找，若要父类初始化，可Parent()
    def parentMed(self):
        print "这是子类覆盖重写的方法，不再调用父类方法"
