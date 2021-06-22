from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('login', views.user_login, name="user_login"),
    path('logout', views.user_logout, name="user_logout"),
    path('team', views.team, name="team"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),

    # Students
    path('view_students',views.view_students,name='view_students'),
    path('add_students',views.add_students,name='add_students'),
    path('delete_student/<int:id>',views.delete_student,name='delete_student'),
    path('edit_student/<int:id>',views.edit_student,name='edit_student'),
    
    # Teachers
    path('view_teachers',views.view_teachers,name='view_teachers'),
    path('add_teachers',views.add_teachers,name='add_teachers'),
    path('delete_teacher/<int:id>',views.delete_teacher,name='delete_teacher'),
    path('edit_teacher/<int:id>',views.edit_teacher,name='edit_teacher'),

    # Librarian
    path('view_librarians',views.view_librarians,name='view_librarians'),
    path('add_librarians',views.add_librarians,name='add_librarians'),
    path('delete_librarian/<int:id>',views.delete_librarian,name='delete_librarian'),
    path('edit_librarian/<int:id>',views.edit_librarian,name='edit_librarian'),

    # Event
    path('view_events',views.view_events,name='view_events'),
    path('add_events',views.add_events,name='add_events'),
    path('delete_event/<int:id>',views.delete_event,name='delete_event'),
    path('edit_event/<int:id>',views.edit_event,name='edit_event'),

    # Timetable
    path('view_timetable',views.view_timetable,name='view_timetable'),

    # Attendance
    path('view_attendance',views.view_attendance,name='view_attendance'),
    path('add_attendance',views.add_attendance,name='add_attendance'),
    path('edit_attendance',views.edit_attendance,name='edit_attendance'),

       
]
