from django.urls import path
from . import views

urlpatterns = [
    path("", views.todo_list, name="todo"),
    path("delete_task/<int:id>/", views.delete, name="delete"),
    path("update_task/<int:id>/",views.update, name="update"),
]
