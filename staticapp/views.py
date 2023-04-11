from django.shortcuts import render

# Create your views here.


def static_app(request):
    return render(request, 'static.html')