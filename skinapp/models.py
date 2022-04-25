from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.utils import timezone



# Create your models here.
class MyAccountManager(BaseUserManager):
    """Manager for user profile."""

    def create_user(self, email, username, password):
        """"Create a new user profile"""
        if not email :
            raise ValueError ('User must have an email address')
        # if not username :
        #     raise ValueError ('User must have a username')

        user = self.model(
        email = self.normalize_email(email),
        username = username,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, username, password):
        """Create and save a super user"""
        user = self.create_user(email = self.normalize_email(email),
        username = username ,
        password = password,
)

        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using = self._db)

        return user

# Create your models here.
class Account(AbstractBaseUser):
    """Database Model for Users in the system"""

    email = models.EmailField( max_length = 255, unique = True)
    username = models.CharField(max_length = 255)
    date_joined = models.DateTimeField( auto_now_add = True)
    last_login = models.DateTimeField( auto_now_add = True)
    is_admin = models.BooleanField (default = False)
    is_active = models.BooleanField (default = True)
    is_staff = models.BooleanField( default = False )
    is_superuser = models.BooleanField (default = False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()


    def __str__(self):
        """"return string representation of our user"""
        return self.email
    def mod(self):
        return self.id


    def has_perm(self, perm, obj=None):
        """"return string representation of our user"""
        return self.is_admin

    def has_module_perms(self, app_label):
        """"return string representation of our user"""
        return True
