from django.shortcuts import render
from datetime import datetime as dt


# Create your views here.
def is_it_newyear(request):
    return render(request, "is_it_christmas.html", {
        "newyear": check_new_year()
    })


# returns true if it's new year
def check_new_year():
    now, new_year = dt.now(), dt(dt.now().year, 1, 1)
    return now == new_year
