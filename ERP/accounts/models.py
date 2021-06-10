from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff = False, is_admin=False, admin_user=False, student_user=False, teacher_user=False, librarian_user=False):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.admin_user = admin_user
        user_obj.student_user = admin_user
        user_obj.teacher_user = admin_user
        user_obj.librarian_user = admin_user
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password = None):
        user = self.create_user(
            email = email, 
            password = password, 
            is_staff = True,
            is_admin= False
        ) 
        return user

    def create_superuser(self, email, password = None):
        user = self.create_user(
            email = email, 
            password = password, 
            is_staff = True,
            is_admin= True
        ) 
        return user

# custom user class
class User(AbstractBaseUser):
    email = models.EmailField(max_length=100,unique=True)
    active = models.BooleanField(default=True) # account is active
    staff = models.BooleanField(default=False) #staff rights
    admin = models.BooleanField(default=False) #admin rights
    admin_user = models.BooleanField(default=False)
    student_user = models.BooleanField(default=False)
    teacher_user = models.BooleanField(default=False)
    librarian_user = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_email(self):
        return self.email
    
    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
    def get_type(self):
        return self.type

class Student(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60,default='')    
    phone_number = models.CharField(max_length=30,default='')
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=100,default='')
    gender = models.CharField(max_length=10,default='')
    fees_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60,default='')    
    phone_number = models.CharField(max_length=30,default='')
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=100,default='')
    gender = models.CharField(max_length=10,default='')
    salary = models.CharField(max_length=30,default='0')
    qualification = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60,default='')    
    phone_number = models.CharField(max_length=30,default='')
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=100,default='')
    gender = models.CharField(max_length=10,default='')
    salary = models.CharField(max_length=30,default='0')

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60,default='')    
    isbn = models.CharField(max_length=50,default='')
    author = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60,default='')    
    description = models.CharField(max_length=50,default='')
    date = models.DateField(null=True)

    def __str__(self):
        return self.name

