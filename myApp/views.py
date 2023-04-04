from django.shortcuts import render
from django.http import HttpResponse as Hp


def Hello(request):
    msg = Hp("Hello Mit")
    return msg


def emobilis(request):
    msg = Hp("This is emobilis")
    return msg


def guidance(request):
    msg = Hp("TO GO TO:\nhello - /hello\nemobilis - /emobilis")
    return msg
# Create your views here.


def home(request):
    return render(request, "home.html")

