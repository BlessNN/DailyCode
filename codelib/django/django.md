
### django基本命令
1. 新建project
django-admin.py startproject project-name
2. 新建app
python manage.py startapp app-name
一般一个项目有多个app
3. 同步数据库


### 基本架构
├── app1
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── models.py    # 数据库相关
│   ├── tests.py
│   ├── views.py     # 定义页面逻辑、内容
├── manage.py
└── project
    ├── __init__.py
    ├── settings.py  # 配置信息，链接project与app之间
    ├── urls.py      # 配置文件，规定访问url及其对应的内容
    ├── wsgi.py

### project解析
urls.py的使用
1. 基本使用范例 
from app1 import views as v # 导入app1的页面设置views.py
urlpatterns = [
    url(r'^$', v.index),  # 解析：访问127.0.0.1/空字符 ，执行v.index方法并返回页面
    url(r'^admin/', admin.site.urls), # 解析:访问127.0.0.1/admin/
]
2. 具体使用
urls.py是用来设置，某一个访问人口url--及其对应的页面内容
第一个参数传入正则表达式，表示一类url
如^表示开头位置，$表示结束位置，'^$'表示空字符
又如'^admin/',表示以admin开头，并且有/的url
3. 进阶使用
此方法使用GET方式，因此可使用值传递
如
127.0.0.1/?a=2&b=8
解释:1 访问127.0.0.1 2传值a和b
另外，在处理页面访问时，可对传入的值进行处理
def add(request):
    a = request.GET['a']
    print ("传入的值a=" + str(a))
    b = request.GET['b']
    return HttpResponse(str(a+b))
4. 高阶使用
url(r'^add/(\d+)/(\d+)/$',app1.views.site)
解释：'\d'表示一个数字，'\d+'一个或多个数字，()表示保存为一个子组，并将每一个子组作为一个参数，被views.py的对应视图函数接收(注意与3用GET接收区分开)
def site(request, ar1, ar2):
    print (str(ar1 + ar2))
    return HttpResponse("ar1 : " + str(ar1))

5. url name的使用
url(r'^add/(\d+)/(\d+)/$',app1.views.site, name='add')
给此网址取个名字，可以通过名字获取此网址
比如django.urls.reverse('add', args=(1,5))
返回u'/add/4/5'
获取add名字的网址，即^add/(\d+)/(\d+)/$,再传入参数1,5，赋值给ar1,ar2；再生成网址返回

### 添加展示网页(使用模板)
在app的文件夹下面添加templates文件夹，放置html页面(最好以不同文件夹区分)
app
├── admin.py
├── __init__.py
├── templates
│   └── baidu.html # 添加要显示的页面
├── views.py

app/views.py:
from django.shortcuts import render
def showBaidu(request):
    return render(request, 'baidu.html') # 使用文件夹要用'lib/baidu.html'

### 模板进阶
类似jsp，在模板上面修改再输出页面
templates/home.html:
{{ aString }}
views.py:
def showPage(request):
    aStr = "views输出给模板，模板处理完再输出显示"
    return render(request , 'home.html', {'aString':aStr})

上面是一个例子，从views输出字符串到模板，模板处理完代码，再输出给用户显示
模板中还可以使用其他函数：
home.html:
for循环
{% for i in TurList %}
{{ i }}
{% endfor %}
显示字典数据(略)
条件判断(略)

