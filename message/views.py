from django.http import HttpResponse


def send_message(request):
    return HttpResponse('<h1>this is some dummy text</h1>')
