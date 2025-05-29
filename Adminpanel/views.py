from django.http import HttpResponse

def index(request):
    return HttpResponse("سلام! این صفحه‌ی اصلی پنل ادمین است.")
