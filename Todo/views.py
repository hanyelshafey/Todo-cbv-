from django.shortcuts import render
from .models import Todo

# Create your views here.












#class based view
from django.views.generic import ListView , DetailView ,CreateView,UpdateView


class Todo_list(ListView):
    model= Todo



class Todo_detail(DetailView):
    model=Todo


class New_todo (CreateView):
    model=Todo


class Edit_todo(UpdateView):
    model=Todo
    fields=['name','detail']
    success_url='/Todo/'

