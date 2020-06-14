from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
import django
from .models import Company

# Create your views here.
#def custom_page_not_found(request): ยังแก้ปัญหา 404 หลัง register ไม่ได้
#    return django.views.defaults.page_not_found(request, None)


def index(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def register(request):
    #return render(request, 'register.html')
    return render(request, 'register_demo.html')

def addUser(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    #repassword = request.POST['repassword']

    User.objects.create_user(
            username = username,
            password = password,
            email = email,
            first_name = firstname,
            last_name = lastname,
            )
    User.save()
    return render(request, 'register_done.html')
'''
    if password == repassword : #เช็คว่า password 2 ช่องตรงกันมั้ย ถ้าตรงไปต่อ
        if User.objects.filter(username=username).exists(): #เช็คว่า username ซ้ำกับที่เคยลงไว้มั้ย
            messages.info(request,'Username นี้มีผู้ใช้แล้ว')
            print("Username นี้มีคนใช้แล้ว")
            return redirect('/register')
        elif User.objects.filter(email=email).exists(): #เช็คว่า email ซ้ำมั้ย
            messages.info(request, 'Email นี้มีผู้ใช้แล้ว')
            print("Email นี้มีผู้ใช้งานแล้ว")
            return redirect('/register')
        else:   #ถ้าไม่ซ้ำ ให้ทำการบันทึกข้อมูล
            User.objects.create_user(
            username = username,
            password = password,
            email = email,
            first_name = firstname,
            last_name = lastname,
            )
            User.save()
            return render(request, 'register_done.html')
    else:   #password ไม่ตรงกัน ลงทะเบียนใหม่
        messages.info(request, 'Password ไม่ตรงกัน')
        return redirect('/register')
'''

def register_done(request):
    return render(request, 'register_done.html')
