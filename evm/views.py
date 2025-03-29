from django.http import HttpResponse


def index(request):
    print(request.path)
    print(request)
    # 业务代码
    data = "<h1>弹性虚拟机首页</h1>"
    return HttpResponse(data, content_type="text/html")
