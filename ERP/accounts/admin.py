from django.contrib import admin
from .models import User, Student, Teacher, Librarian, Book, Event, Attendance

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Librarian)
admin.site.register(Book)
admin.site.register(Event)
admin.site.register(Attendance)
