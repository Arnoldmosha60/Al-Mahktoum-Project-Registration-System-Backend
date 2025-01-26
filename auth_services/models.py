from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, name, email, password=None, national_id_number=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number field is required")
        if not name:
            raise ValueError("The Name field is required")
        if not email:
            raise ValueError("The Email field is required")

        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, name=name, email=email, national_id_number=national_id_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, email, password=None, national_id_number=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, name, email, password, national_id_number, **extra_fields)

# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    national_id_number = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(("Male", "Male"), ("Female", "Female")))
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'email', 'gender']

    def __str__(self):
        return self.phone_number