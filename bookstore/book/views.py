from django.shortcuts import render,render_to_response, redirect
from django.http import HttpResponse
from django import forms
# Create your views here.
from .models import Book

class bookForm(forms.Form):
    bookName = forms.CharField(max_length=20)
    bookDetail = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'size': 200}))
    bookImage = forms.ImageField()
    price = forms.DecimalField(max_digits=5, decimal_places=2)
    course = forms.CharField(max_length=20)
    teacher = forms.CharField(max_length=5)



def index(request):
    return HttpResponse("This is the index of Books!")

def addBook(request):
    print(request.session['userID'])
    if ( not request.session.has_key('userID')):
        return redirect('/account/login')

    if request.method == "POST":
        bf = bookForm(request.POST)
        print(bf)
        if bf.is_valid():
            print(bf)
            return HttpResponse("Success")
    else:
        bf = bookForm()
        return render(request, 'book/addBook.html',{'bf':bf})

