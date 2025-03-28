from django.http import JsonResponse

def hello(request):
    print(1111)
    return JsonResponse({'status': 1,'hello': 'world'})