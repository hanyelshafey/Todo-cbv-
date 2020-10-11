from django.urls import path
from . import views
app_name = 'Todo'

urlpatterns = [
    path('', views.Todo_list.as_view(),name='todolist'),
    path('cbv/<int:pk>', views.Todo_detail.as_view(),name='tododetails'),
    path('cbv/New', views.New_todo.as_view(),name='New'),
    path('cbv/<int:pk>/edit', views.Edit_todo.as_view(),name='edit'),


]