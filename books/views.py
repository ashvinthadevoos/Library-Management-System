from django.shortcuts import render,redirect
from django.views import View
from books import forms,models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

class BookCreateView(View):
    def get(self,request,*args,**kwargs):
        form=forms.BookCreateForm()
        return render(request,'bookcreate.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=forms.BookCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('list')
        return render(request,'bookcreate.html',{'form':form})

class BookListView(View):
    def get(self,request,*args,**kwargs):
        qs=models.Books.objects.all()
        return render(request,'booklist.html',{'data':qs})
    
class BookEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=models.Books.objects.get(id=id)
        form=forms.BookCreateForm(instance=qs)
        return render(request,'bookcreate.html',{'form':form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get('id')
        qs=models.Books.objects.filter(id=id,is_active=True)
        form=forms.BookCreateForm(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request,'bookcreate.html',{'form':form})
    
class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        models.Books.objects.filter(id=id).update(is_active=False)
        return redirect('list')


class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=forms.LoginForm()
        return render(request,'login.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)
        print(form)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect('list')
        return render(request,'login.html',{'form':form})
    
class SignupView(View):
    def get(self,request,*args,**kwargs):
        form=forms.SignupForm()
        return render(request,'signup.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=forms.SignupForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            uname=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect('list')
        return render(request,'signup.html',{'form':form})    