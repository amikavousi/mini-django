from django.template.response import TemplateResponse
from .models import Message
from django.http import HttpResponse


def message(request):
    messages = Message.objects.all()
    context = {
        'messages': messages
    }
    return TemplateResponse(request, 'index.html', context)

