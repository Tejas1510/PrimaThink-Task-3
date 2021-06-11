from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .models import Student, Teacher, Librarian, User, Event
from .forms import CustomUserCreationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def home(request):
    return render(request, 'index.html', {})


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(email=email, password=password)
        print('USER: ', str(user), "Email: ", email, "password: ", password)
        if user is not None and user.is_active:
            # Login Successfull
            login(request, user)
            return redirect('home')
        else:
            # Login Unsuccessfull , Show Same Page With Error
            return render(request, 'login.html', {'loginStatus': "Incorrect Credentials."})
    else:
        if request.user.is_authenticated:
            # If user is already logged in, send to home
            return redirect('home')
        # Display Login Page
        return render(request, 'login.html', {})


def user_logout(request):
    print("logout method: " + str(request.user) + " : " + str(request.user.is_active))
    if request.user is not None and request.user.is_active:
        logout(request)
        print("after logout user = " + str(request.user))
        return render(request, 'logout.html', {})
    else:
        return redirect('user_login')



################  Student Views ############################

def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_student.html', {'students': students})


def add_students(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = name+"@12345"
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        fees_paid = request.POST.get('fees_paid')
        if fees_paid.lower() == "paid":
            fees_paid = True
        else:
            fees_paid = False
        user = User.objects.create_user(
            email=email, password=password, student_user=True)
        student = Student(name=name, user=user, phone_number=phone_number, address=address,
                          date_of_birth=date_of_birth, gender=gender, fees_paid=fees_paid)
        student.save()
        return redirect('view_students')
    else:
        return render(request, 'add_student.html')


def delete_student(request, id):
    students = Student.objects.all()
    student = Student.objects.get(profile_id=id)
    student.user.delete()
    return redirect('view_students')


def edit_student(request, id):
    student = Student.objects.get(profile_id=id)
    student.name = request.POST.get('nameEdit')
    student.phone_number = request.POST.get('mobileEdit')
    student.address = request.POST.get('addressEdit')
    student.date_of_birth = request.POST.get('dobEdit')
    student.gender = request.POST.get('genderEdit')
    fee = request.POST.get('feeEdit')
    print(str(request.POST))
    if fee.lower() == "paid":
        student.fees_paid = True
    else:
        student.fees_paid = False
    student.save()
    return redirect('view_students')


################  Teacher Views ############################


def view_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'view_teacher.html', {'teachers': teachers})


def add_teachers(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = name+"@12345"
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        salary = request.POST.get('salary')
        qualification = request.POST.get('qualification')

        user = User.objects.create_user(
            email=email, password=password, teacher_user=True)
        teacher = Teacher(name=name, user=user, phone_number=phone_number, address=address,
                          date_of_birth=date_of_birth, gender=gender, salary=salary, qualification=qualification)
        teacher.save()
        return redirect('view_teachers')
    else:
        return render(request, 'add_teacher.html')


def delete_teacher(request, id):
    teachers = Teacher.objects.all()
    teacher = Student.objects.get(profile_id=id)
    teacher.user.delete()
    return redirect('view_teachers')

def edit_teacher(request, id):
    teacher = Teacher.objects.get(profile_id=id)
    teacher.name = request.POST.get('nameEdit')
    teacher.phone_number = request.POST.get('mobileEdit')
    teacher.address = request.POST.get('addressEdit')
    teacher.date_of_birth = request.POST.get('dobEdit')
    teacher.salary = request.POST.get('salaryEdit')
    teacher.qualification = request.POST.get('qualificationEdit')
    teacher.save()
    return redirect('view_teachers')


################  librarian Views ############################

def view_librarians(request):
    librarians = Librarian.objects.all()
    return render(request, 'view_librarian.html', {'librarians': librarians})


def add_librarians(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = name+"@12345"
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        salary = request.POST.get('salary')

        user = User.objects.create_user(
            email=email, password=password, librarian_user=True)
        librarian = Librarian(name=name, user=user, phone_number=phone_number,
                              address=address, date_of_birth=date_of_birth, gender=gender, salary=salary)
        librarian.save()
        return redirect('view_librarians')
    else:
        return render(request, 'add_librarian.html')


def delete_librarian(request, id):
    librarians = Librarian.objects.all()
    librarian = Librarian.objects.get(profile_id=id)
    librarian.user.delete()
    return redirect('view_librarians')

def edit_librarian(request, id):
    librarian = Librarian.objects.get(profile_id=id)
    librarian.name = request.POST.get('nameEdit')
    librarian.phone_number = request.POST.get('mobileEdit')
    librarian.address = request.POST.get('addressEdit')
    librarian.date_of_birth = request.POST.get('dobEdit')
    librarian.salary = request.POST.get('salaryEdit')
    librarian.save()
    return redirect('view_librarians')


################ Event Views ############################

def view_events(request):
    event = Event.objects.all()
    blogposts = []

    paginator = Paginator(event, 3)
    page = request.GET.get('page')
    try:
        events = paginator.get_page(page)

    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return render(request, 'view_event.html', {'events': events})


def add_events(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        image = request.POST.get('image')
        url = request.POST.get('url')

        event = Event(name=name, description=description,
                      date=date, time=time, image=image, url=url)
        event.save()
        return redirect('view_events')
    else:
        return render(request, 'add_event.html')


def delete_event(request, id):
    event = Event.objects.all()
    event = Event.objects.get(profile_id=id)
    event.user.delete()
    return redirect('view_events')

def edit_event(request, id):
    event = Event.objects.get(event_id=id)
    event.name = request.POST.get('nameEdit')
    event.description = request.POST.get('descriptionEdit')
    event.date = request.POST.get('dateEdit')
    event.time = request.POST.get('timeEdit')
    event.image = request.POST.get('imageEdit')
    event.url = request.POST.get('urlEdit')
    event.save()
    return redirect('view_events')
