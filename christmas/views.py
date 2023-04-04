from django.shortcuts import render
from datetime import datetime as dt


# Create your views here.
def is_it_christmas(request):
    return render(request, "is_it_christmas.html", {
        "christmas": check_christmas()
    })


# returns true if it's new year
def check_christmas():
    now, christmas = dt.now(), dt(dt.now().year, 12, 25)
    return now == christmas
