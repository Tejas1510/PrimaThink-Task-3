from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.user_login, name="user_login"),

    # Students
    path('view_students',views.view_students,name='view_students'),
    path('add_students',views.add_students,name='add_students'),
    path('delete_student/<int:id>',views.delete_student,name='delete_student'),
    
    # Teachers
    path('view_teachers',views.view_teachers,name='view_teachers'),
    path('add_teachers',views.add_teachers,name='add_teachers'),
    path('delete_teacher/<int:id>',views.delete_teacher,name='delete_teacher'),

    # path('library',views.library,name='library'),
     # path('events',views.events,name='events'),
]
