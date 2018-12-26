from django.shortcuts import render

# Create your views here.


def Background(request):
    return render(request, 'background.html')


def leave(request):
    return render(request, 'leave.html')
