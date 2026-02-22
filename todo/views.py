from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDo

def todo_list(request):
    tasks = ToDo.objects.all()
    if request.method == "POST":
            title = request.POST.get("title")
            if title:
                ToDo.objects.create(title = title)
            return redirect("todo")
    return render(request, "todo.html", {"tasks":tasks})


def delete(request, id):
    if request.method== "POST":
        tasks = get_object_or_404(ToDo, id = id)
        tasks.delete()
    return redirect("todo")

def update(request, id):
    tasks = get_object_or_404(ToDo, id=id)
    if request.method =="POST":
        new_title = request.POST.get("title")
        if new_title:
            tasks.title = new_title
            tasks.save()
        return redirect("todo")
    return render(request,"update.html",{"tasks":tasks})