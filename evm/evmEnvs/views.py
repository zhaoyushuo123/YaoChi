from django.http import HttpResponse


def index(request):
    print(request.path)
    print(request)
    # 业务代码
    data = "<h1>弹性云环境</h1>"
    return HttpResponse(data, content_type="text/html")

def evmList(request):
    print(request.path)
    print(request)
    # 业务代码
    data = "<h1>6666666</h1>"
    return HttpResponse(data, content_type="text/html")
