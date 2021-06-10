from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .models import Student,Teacher,User
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {})
    
def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        user = authenticate(email=email, password=password)
        print('USER: ', str(user),"Email: ",email, "password: ", password)
        if user is not None and user.is_active:
            # Login Successfull
            login(request, user)
            return render(request, 'home.html', {})
        else:
            # Login Unsuccessfull , Show Same Page With Error
            return render(request, 'login.html', {'loginStatus':"Incorrect Credentials."})
    else:
        if request.user.is_authenticated:
            # If user is already logged in, send to home
            return render(request, 'home.html', {})
        # Display Login Page
        return render(request, 'login.html', {})


################  Student Views ############################

def view_students(request):
    students=Student.objects.all()
    return render(request, 'view_student.html', {'students':students})

def add_students(request):
    students=Student.objects.all()
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=name+"@gmail.com"
        phone_number=request.POST.get('phone_number')
        address=request.POST.get('address')
        date_of_birth=request.POST.get('date_of_birth')
        gender=request.POST.get('gender')
        fees_paid=request.POST.get('fees_paid')
        user=None
        user_form=CustomUserCreationForm(email=email,password1=password,password2=password)
        if user_form.is_valid():
            user=user_form.save()
            user.student_user=True
            user.save()
            print("Data Saved")
        
        student=Student(name=name,user=user,phone_number=phone_number,address=address,date_of_birth=date_of_birth,gender=gender,fees_paid=fees_paid)
        return render(request, 'view_student.html', {'students':students})
    else:
        return render(request, 'add_student.html', {'students':students})

def delete_student(request,id):
    students=Student.objects.all()
    student=Student.objects.get(id=id)
    student.delete()
    return render(request, 'view_student.html', {'students':students})


################  Teacher Views ############################

def view_teachers(request):
    teachers=Teacher.objects.all()
    return render(request, 'view_teacher.html', {'teachers':teachers})

def add_teachers(request):
    teachers=Teacher.objects.all()
    if request.method == "POST":
        return render(request, 'view_teacher.html', {'teachers':teachers})
    else:
        return render(request, 'add_teacher.html', {'teachers':teachers})

def delete_teacher(request,id):
    teachers=Teacher.objects.all()
    teacher=Student.objects.get(id=id)
    teacher.delete()
    return render(request, 'view_teacher.html', {'teachers':teachers})