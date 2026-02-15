from django.shortcuts import render,redirect
from django.views import View
from books import forms,models

# Create your views here.

class BookCreateView(View):
    def get(self,request,*args,**kwargs):
        form=forms.BookCreateForm()
        return render(request,'bookcreate.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=forms.BookCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('create')
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


    