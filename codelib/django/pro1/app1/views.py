#coding=utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse(u"This is testing 测试页面")

def testHtml(request):
    return render(request, 'baidu.html')
