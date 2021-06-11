from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.user_login, name="user_login"),
    path('logout', views.user_logout, name="user_logout"),

    # Students
    path('view_students',views.view_students,name='view_students'),
    path('add_students',views.add_students,name='add_students'),
    path('delete_student/<int:id>',views.delete_student,name='delete_student'),
    
    # Teachers
    path('view_teachers',views.view_teachers,name='view_teachers'),
    path('add_teachers',views.add_teachers,name='add_teachers'),
    path('delete_teacher/<int:id>',views.delete_teacher,name='delete_teacher'),

    # Librarian
    path('view_librarians',views.view_librarians,name='view_librarians'),
    path('add_librarians',views.add_librarians,name='add_librarians'),
    path('delete_librarian/<int:id>',views.delete_librarian,name='delete_librarian'),


    # path('library',views.library,name='library'),
     # path('events',views.events,name='events'),
]
