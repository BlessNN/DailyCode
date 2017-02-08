
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
    print num  ## 输出失败，必须使用global num ,print num
    num = 9
num = 10
pri_num()  ## 使用global 则输出num=10
print num  ## num =9,在函数pri_num中改变了num的值

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

