from django.shortcuts import render, redirect
from .models import ToDo
def todo(request):
    todo= ToDo.objects.all()
    
    if request.method == "POST":
        if "add_task" in request.POST:
            title = request.POST.get("title")
            if title:
                ToDo.objects.create(title=title)
            return redirect("todo")
            
    return render(request, "todo.html",{"todo":todo})