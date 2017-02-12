### 常用操作
dir(person) # 查看对象的所有属性和方法
type(var)   # 查看变量类型
help(obj)   # 查看此类的帮助手册

### 变量类型
变量名对应指针，变量对应一块内存空间
eg:
ai=12
bi=12
id(ai)是否等于id(bi)?
是，因为12是整型变量，存放在一个内存空间，并且不重复
cc="12"
id(ai)是否等于id(cc)? 
不，因为type(cc)=>str，“12”是字符串变量，不同于12整型变量
#### 删除变量及其回收
del ai ## 删除ai变量，即删除指针对内存值的指向，并此内存值的引用数减1
什么时候回收内存空间？
每隔一段时间检查内存值的引用数，引用数为0的内存空间删除

#### 特殊变量
__XXX__ 系统定义的变量
__XXX   类的本地变量
_XXX   from module import *
#### 全局变量与局部变量
def pri_num():
    print num  ## 输出失败，*必须使用global num* ,print num
    num = 9
num = 10
pri_num()  ## 使用global 则输出num=10
print num  ## num =9,在函数pri_num中改变了num的值

执行函数
gloals() # 可以查看此程序现有的全局变量
locals() # 可以查看现有局部变量，返回字典变量
#### 逻辑表达式
not flag  非
fa and fb 与
fa or fb  或
a is b    a和b是同一个对象
### 关系表达式
==
！=
>
<
### 分支语句
if a>b:
    print a
elif a=b:
    print "equal"
else:
    print b

for fruit in frus:  ## for可以遍历列表、tuple、dictionary或者字符串
    print fruit

while a>b:
   print a

break
continue

### list列表（类似数组）
aList = [1,5,'hello'] ## 数据元素可存放不同类型变量
aList[-1]  ## 倒数第一个
aList[下限:上限:步长] ## 找出下限制到上限中，每几步一个变量
aList * 3
aList1 + aList2 拼接列表
del aList[2]    删除一个元素
总结：无论是分片还是链接操作，都已经实现
列表其他常用方法：
cmp(list1, list2)
len(list1)
max(list1)
min(list1)
list(seq) ## 讲元祖转换为列表
aList.append('new var')
aList.pop()
aList.remove(obj) ## 移除第一个匹配值
aList.reverse()   ## 反向列表中元素
aList.sort([func])

### 元祖Tuple（类似列表，但元祖的元素不能修改--只读的列表）
aTup=(1,5,8,2,'tuple',33.3)
总结：对比列表，不能修改、删除某个元素

### 字典(键值对)，类似Json
dict = { 'Alice':'19', 'Beth':'20', 'Cyle' }
dict['Beth']=21   ## 可修改
del dict['Cyle']  ## 可删除
注意：1、键值具有唯一性，不能重复  2、键必须不可变，可以用数字、字符串或者tuple但是不能用列表 3、值可以是任意对象
字典内置函数&方法：
cmp(dict1, dict2)
str(dict)
len(dict)
dict.keys()  # 输出所有键
dict.values() # 输出所有值
dict.clear()
dict.copy()
dict.get(key)
dict.items()  # 以列表形式返回此字典
dict.update(dict2) # 吧字典dict2的键值对更新到dict里面

### 字符串
str = 'ABC' "ABC" '''CDE'''  """EFG"""
以上的引号方式都能表示一个字符串，但'""'的复合使用能表示字符串中的引号，"""允许字符串带换行
字符串也能看成一个列表(数组)，使用如Str[5:8]的形式

### 函数
1. test.py
#Function definition is here
def prime(str):
    print str
可以使用help(test.prime),会打印出Function definition
2. 单个变量按值传递；list等按引用传递
def changme(var):
    var = "Changed"
    return   # 无返回任何变量
list=[1,2,3]
changme(list) 
print list # 输出list="changed"

var = 0
changme(var)
print var # var = 0
3. 函数参数
用法1：def check(id, name):
调用时check(343,"Jack")
id和name为必备参数，调用时必须输入
用法2:
调用时check(name="Jack",343)
可指定参数名，先后顺序可任意
用法3：缺省参数
def get(name,age=10):
调用可以get('Mike',5)或者get('Mike')
此时,age参数不输入则为默认值
用法4：不定长参数
def arg(a,b,*c):
    print c
arg(1,1,34,56) # 打印:1,1，(34,56)
除了a，b必须传入之外，后面可传入任意个参数，全部变成元祖c的元素
def arg(name,**parents):
    print name+':'+str(parents)
arg('Jay',dad='Jack',mom='July') # 打印：Jay: {dad='Jack',mom='July'}
除了name必须传入，后面可传入任意多个指定参数，全部变成字典parents


### Class
class Employee:
    '''
    For help info
    '''
    classspec = "testing class"i # 类静态变量

    def __init__(self, name, pay): # 构造函数
        self.com = "Baidu"  # 类的属性,默认赋值
        self.name = name    # 类的属性
        self.pay = pay      # 类的属性
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
##############################
Function：通过名字可以调用一段代码，可以传参数进去并得到返回值，所有的参数都是明确传递过去的。
Method：是Function和对象的结合。调用一个方法，有些参数是隐含传递过去的。具体来说分三种Method
1. instance method (必须带有self为第一个参数)必须绑定实例化对象才能调用，即常用的对象的方法，可使用实例对象的属性、静态变量，如e.say()
2. class method    (必须带有cls为第一个参数)静态方法，依靠类存在的方法，通过类来调用，可使用类的静态变量如Employee.clsSay()  
3. static method   实际就是一个函数，不依靠类的存在，写在类外面一样正常使用，但不能使用此类中的所有属性,如Employ.stcSay()
*****************************
Attribute:类中存在的变量(属性)可以分为两种：
1. 类的变量(静态属性)
比如classspec = "testing class"
class method和instance Method可以调用，或者直接在类外部Employee.classspec访问
(当然，如果是定义为__classspec私有静态属性，类外部就访问不了)
2. 实例化对象的变量(属性)
比如self.com,self.name,self.pay等
只有实例化后新建一个具体对象才存在，因此只有instance Method可以调用
############################
类的私有属性
__var # 以__开头的属性
类的私有方法(即设置instance method的权限为私有)
def __med(self[,arg...]): 
**************************
默认自带内置类属性
print Employee.__dict__   # 类的所有属性
print Employee.__doc__
print Employee.__module__
另外也有自带方法，如：
def __init__(self[,arg..]) #构造函数
def __del__(self[,arg..])  #删除对象时调用函数
def __str__(self[,arg..])  #实例对象字符串化输出
###########################
python内部记录着所有使用中的对象各有多少引用。
一个内部跟踪变量，成为一个引用计数器。当对象创建就创建了一个引用技术，当这个对象del 时候计数器减1，当这个实例对象的引用技术变为0时，被垃圾回收(非立即，在适当时机)
############################
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
**************************
import 模块
比如import os # 可以直接调用系统的命令，如os.mkdir, os.chmod
导入的模块名存放在PYTHONPATH环境变量中，类似shell中的PATH
执行py程序时，按照Pythonpath变量中的路径寻找对应模块
(注意命名冲突可能发生，有时同个目录下有同名导入模块文件名，由于Pythonpath默认.为最优先查找目录，导致导入模块失败)
**************************
模块可以是一个包(包含多个函数)，可以是一个py文件
import os  #导入方式一，整个模块
os.mkdir...
from math import sqrt  # 导入方式二，只导入某个函数
sqrt(4)...

#### 文件操作
1. 打印、读取输入
raw_input() # 读取一行字符串，并以字符串返回
input()     # 读取一行字符串，以Python合法形式返回(读到10则返回整形变量)

print # 对输出的文本做自动编码转换(参照现环境变量输出)；可以按一定格式输出

2. 文件
file_obj = open("路径+文件","指定读写模式") # r只读，r+读写，w新建，a追加，b二进制文件
文件常用操作：
file_obj.readline()
f.write("Something")
f.flush() # 三种刷新缓冲区到文件方法：1flush 2缓冲区满了 3文件close
f.close()
f.seek()  # 调节指针位置 
属性：
f.closed # 是否关闭文件
f.mode   # 文件访问模式
f.name   # 返回文件名称


