from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Student, Teacher, Librarian, User, Event, Attendance,TimeTable
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
# Create your views here.


def user_validator(request):
    if request.user is not None and request.user.is_active:
        if request.user.admin_user:
            return "ADMIN"
        elif request.user.student_user:
            return "STUDENT"
        elif request.user.teacher_user:
            return "TEACHER"
        elif request.user.librarian_user:
            return "LIBRARIAN"
    return "ERROR"



def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(email=email, password=password)
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
    if request.user is not None and request.user.is_active:
        logout(request)
        return redirect('index')
    else:
        return redirect('user_login')

def index(request):
    if request.user is not None and request.user.is_active:
        a=True
        return render(request, 'index.html',{'log':a})
    else:
        return render(request, 'index.html')

def team(request):
    if request.user is not None and request.user.is_active:
        a=True
        return render(request, 'team.html',{'log':a})
    else:
        return render(request, 'team.html')

def contact(request):
    if request.user is not None and request.user.is_active:
        a=True
        return render(request, 'contact.html',{'log':a})
    else:
        return render(request, 'contact.html')

def about(request):
    if request.user is not None and request.user.is_active:
        a=True
        return render(request, 'about.html',{'log':a})
    else:
        return render(request, 'about.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def home(request):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    student=Student.objects.all()
    teacher=Teacher.objects.all()
    event=Event.objects.all()
    librarian=Librarian.objects.all()

    return render(request, 'home.html', {'s':len(student),'t':len(teacher),'e':len(event),'l':len(librarian)})
################  Student Views ############################
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def view_students(request):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    students = Student.objects.all()
    return render(request, 'view_student.html', {'students': students})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def add_students(request):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
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


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def delete_student(request, id):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    student = Student.objects.get(profile_id=id)
    student.user.delete()
    return redirect('view_students')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def edit_student(request, id):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    student = Student.objects.get(profile_id=id)
    student.name = request.POST.get('nameEdit')
    student.phone_number = request.POST.get('mobileEdit')
    student.address = request.POST.get('addressEdit')
    student.date_of_birth = request.POST.get('dobEdit')
    student.gender = request.POST.get('genderEdit')
    fee = request.POST.get('feeEdit')
    if fee.lower() == "paid":
        student.fees_paid = True
    else:
        student.fees_paid = False
    student.save()
    return redirect('view_students')


################  Teacher Views ############################

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def view_teachers(request):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    teachers = Teacher.objects.all()
    return render(request, 'view_teacher.html', {'teachers': teachers})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def add_teachers(request):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
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


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def delete_teacher(request, id):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    teacher = Teacher.objects.get(profile_id=id)
    teacher.user.delete()
    return redirect('view_teachers')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def edit_teacher(request, id):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
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
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def view_librarians(request):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    librarians = Librarian.objects.all()
    return render(request, 'view_librarian.html', {'librarians': librarians})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def add_librarians(request):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
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


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def delete_librarian(request, id):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    librarian = Librarian.objects.get(profile_id=id)
    librarian.user.delete()
    return redirect('view_librarians')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def edit_librarian(request, id):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    librarian = Librarian.objects.get(profile_id=id)
    librarian.name = request.POST.get('nameEdit')
    librarian.phone_number = request.POST.get('mobileEdit')
    librarian.address = request.POST.get('addressEdit')
    librarian.date_of_birth = request.POST.get('dobEdit')
    librarian.salary = request.POST.get('salaryEdit')
    librarian.save()
    return redirect('view_librarians')


################ Event Views ############################
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def view_events(request):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    event = Event.objects.all()

    paginator = Paginator(event, 3)
    page = request.GET.get('page')
    try:
        events = paginator.get_page(page)

    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return render(request, 'view_event.html', {'events': events})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def add_events(request):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
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


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def delete_event(request, id):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    event = Event.objects.all()
    event = Event.objects.get(profile_id=id)
    event.user.delete()
    return redirect('view_events')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def edit_event(request, id):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    event = Event.objects.get(event_id=id)
    event.name = request.POST.get('nameEdit')
    event.description = request.POST.get('descriptionEdit')
    event.date = request.POST.get('dateEdit')
    event.time = request.POST.get('timeEdit')
    event.image = request.POST.get('imageEdit')
    event.url = request.POST.get('urlEdit')
    event.save()
    return redirect('view_events')


################ Timetable View ############################
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def view_timetable(request):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    if request.method == "POST":
        TimeTable.objects.all().delete()
        timetable=request.FILES['pic']
        tt = TimeTable(timetable_image=timetable)
        tt.save()
        return redirect('view_timetable')
    else:
        tt = TimeTable.objects.all()
        return render(request, 'timetable.html', {'t_image':tt[0]})


################  Attendance Views ############################

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def view_attendance(request):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    if request.method == "POST":
        date = request.POST.get('date')
        attendance = Attendance.objects.filter(date=date)        
        return render(request, 'view_attendance.html', {'attendance': attendance, 'date': date})
    else:
        return render(request, 'view_attendance.html', {})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def add_attendance(request):
    if user_validator(request) != "ADMIN":
        return render(request, 'entry_restricted.html', {})
    if request.method == "POST":

        date = request.POST.get('date')
        studentList = Student.objects.all()
        if len(Attendance.objects.filter(date=date)) == 0:
            for i in studentList:            
                attendance = request.POST.get('attend' + str(i.profile_id))
                x = None
                if attendance.lower() == "present":
                    x = Attendance(student=i, date=date, attend=True)
                else:
                    x = Attendance(student=i, date=date, attend=False)
                x.save()
        else:
            return redirect('add_attendance')
        return redirect('view_attendance')
    else:
        students = Student.objects.all()
        return render(request, 'add_attendance.html', {'students': students})



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='user_login')
def edit_attendance(request):
    if request.method == "POST":
        date = request.POST.get('dateEdit')
        email = request.POST.get('emailEdit')
        attendance = request.POST.get('attendEdit')
        record = list(Attendance.objects.filter(student__user__email__contains=email, date=date))[0]
        if attendance.lower() == "present":
            record.attend = True
        else:
            record.attend = False
        record.save()
    return redirect('view_attendance')