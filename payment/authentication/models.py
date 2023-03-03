from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password

# CREATES A CUSTOM MODEL BY INHERITING FROM DJANGO USER MANAGER


class MyUserManager(UserManager):
    def _create_user(self, full_name, email, password, **extra_fields):
        """
        Create and save a user with the given full_name, email, and password.
        """
        if not full_name:
            raise ValueError("The given full_name must be set")
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        user = self.model(full_name=full_name, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, full_name, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(full_name, email, password, **extra_fields)

    def create_superuser(self, full_name, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(full_name, email, password, **extra_fields)

#  creates a User model defined with the following fields and uses the custom MyUserManager to override the Username Field to use email as the unique identifier


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300, unique=True, db_index=True)
    sex = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.email
