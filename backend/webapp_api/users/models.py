from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None, is_staff=False, is_admin=False, is_active=True):

        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        if not password:
            raise ValueError('Users must have an password')

        if not username:
            raise ValueError('Users must have an username')

        user_obj = self.model(
            email= self.normalize_email(email),
        )
        user_obj.username = username 
        user_obj.set_password(password)
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, email, first_name, last_name, password=None, is_active=True):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username = username, 
            email = email,
            password=password,
            is_staff = True
        )        
        return user

    def create_superuser(self, username, email, first_name, last_name, password=None, is_active=True):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username = username, 
            email = email,
            first_name = first_name,
            last_name = last_name,
            password=password,
            is_staff = True,
            is_admin = True
        )
        return user



class User(AbstractBaseUser):
    first_name          = models.CharField(max_length=120, blank = True, null = True)
    last_name           = models.CharField(max_length=120)
    username            = models.CharField(max_length=120, unique=True)
    USERNAME_FIELD      = 'username' #set username
    timestamp           = models.DateTimeField(auto_now_add=True)
    
    email  = models.EmailField(verbose_name='Email Address', max_length=255,unique=True)
    active = models.BooleanField(default=True)
    staff  = models.BooleanField(default=False) # a admin user; non super-user
    admin  = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email'] # Email & Password are required by default.

    objects = UserManager()

    def get_username(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    