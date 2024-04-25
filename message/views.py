from django.shortcuts import render


def message(request):
    return render(request, 'index.html')

