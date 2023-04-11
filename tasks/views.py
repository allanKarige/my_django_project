from django.shortcuts import render

tasks = ["Eat food", "Wash the dishes", "Take out the trash", "Make some pie"]
# Create your views here.


def task(request):
    return render(request, "tasks.html", {
        "tasks": tasks
    })


def add(request):
    return render(request, "add.html")

