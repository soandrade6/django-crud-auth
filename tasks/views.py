from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def helloworld(request):
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })


