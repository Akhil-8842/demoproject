from django.shortcuts import render,redirect
from django.views.generic import TemplateView, CreateView,ListView,DetailView,View

# from library.books.views import viewbooks

#
# class based
# view
# updateview
# view
# templateview
# listview
# detailview
# deleteview


from django.views.generic import TemplateView
class Home(TemplateView):
    template_name = "home.html"

from app1.models import School
from django.urls import reverse_lazy
from app1.forms import Schoolform

class AddSchool(CreateView):
    model=School
    # fields=['name','location','principal']
    form_class = Schoolform
    template_name = "addschool.html"
    success_url = reverse_lazy('home')

from app1.models import Student
from django.urls import reverse_lazy


class AddStudent(CreateView):
    model=Student
    template_name = "addstudent.html"
    fields=['name','age','school']
    success_url = reverse_lazy('home')


class SchoolList(ListView):
    model=School
    template_name = 'list.html'
    context_object_name = 'schools'

    def get_queryset(self):
        qs=super().get_queryset()
        queryset=qs.filter(location="Ernakulam")
        return queryset




class StudentList(ListView):
    model=Student
    template_name = 'stulist.html'
    context_object_name = 'students'

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(school__location="Ernakulam")# fore
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(name__icontains="nu")
    #     return queryset

    #
    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(age__gt="13")
    #     return queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(age__it="13")
    #     return queryset


    def get_queryset(self):
        qs=super().get_queryset()
        queryset=qs.filter(name__startswith="a")
        return queryset

    #get_context_data
    def get_context_data(self):
        context=super().get_context_data()
        context['name']='Arun'
        context['school']=School.objects.all()
        return context




class Schooldetails(DetailView):
    model=School
    template_name = 'schooldetail.html'
    context_object_name = 'schools'


from django.contrib.auth.models import User
class Register(CreateView):
    model=User
    fields=['username','password','email','first_name','last_name']
    template_name = "register.html"
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        u = form.cleaned_data['username']
        p = form.cleaned_data['password']
        e = form.cleaned_data['email']
        f = form.cleaned_data['first_name']
        l = form.cleaned_data['last_name']

        u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
        u.save()
        return redirect('home')

from django.contrib.auth.views import LoginView
class Login(LoginView):
    template_name="login.html"
from django.contrib.auth import logout
from django.views.generic import View
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')