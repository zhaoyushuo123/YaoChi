from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.views.decorators.http import require_http_methods

"""
require_http_methods 用于限制用户访问函数视图的http请求方法
"""


@require_http_methods(['POST', 'GET'])
# Create your views here.
def index(request):
    print(request.path)
    print(request)
    # 业务代码
    data = "<h1>ok!!!!</h1>"
    return HttpResponse(data, content_type="text/html")

@require_http_methods(['GET'])
def goods(request):
    print(request)
    return HttpResponse("<h1>goods!!!</h1>")