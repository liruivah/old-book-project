from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.template import RequestContext
from django.contrib import auth

from .models import User
# Create your views here.

def index(request):
    return HttpResponse("Hello, This is the BookStore.")

class UserLoginForm(forms.Form):
    username = forms.CharField( max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)

class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=10)
    password1 = forms.CharField(label='password',widget=forms.PasswordInput())
    password2 = forms.CharField(label='repassword',widget=forms.PasswordInput())
    email = forms.EmailField(label='email')
    dept = forms.CharField(label='dept',max_length=15)
    phone = forms.CharField(label='phone',max_length=11)

def login(request):
    if request.method == "POST":
        print(request.POST)
        uf = UserLoginForm(request.POST)
        if uf.is_valid():
            #get form info
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            userResult = User.objects.filter(username = username,password = password)

            if (len(userResult) > 0):
                context = {
                    'operation':'login'
                }
                request.session['userID'] = userResult[0].pk
                print(userResult[0].pk)
                return render_to_response('success.html', context)
            else:
                return HttpResponse("该用户不存在")
    else:
        uf = UserLoginForm()
        return render_to_response("userlogin.html",{'uf':uf})

def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            filterResult = User.objects.filter(username=username)
            if (len(filterResult) > 0):
                return render_to_response('register.html',{'errors': 'uername exists'})
            else:
                password1 = uf.cleaned_data['password1']
                password2 = uf.cleaned_data['password2']
                if (password1 != password2):
                    return render_to_response('register.html',{'errors': 'password'})
                email = uf.cleaned_data['email']
                dept = uf.cleaned_data['dept']
                phone = uf.cleaned_data['phone']
                user = User.objects.create(username=username,password=password1,email=email,dept=dept,phone=phone)
                user.save()
                return render_to_response('success.html', {'username':username,'operation':"register"})
    else:
        uf = UserForm()
        return render(request, 'register.html',{'uf':uf})
