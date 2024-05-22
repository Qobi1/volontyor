from django.core.validators import EmailValidator
from django.db import models
from django.utils.text import slugify
import random
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser, User
from django.db import models
from django.utils import timezone


# class CustomUserManager(BaseUserManager):
#     def create_user(self, phone_number, password=None, **extra_fields):
#         if not phone_number:
#             raise ValueError('The Phone Number field must be set')
#         email = self.normalize_email(phone_number)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(email, password, **extra_fields)
#
#
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     phone_number = models.TextField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = []
#
#     def __str__(self):
#         return self.phone_number


class Event(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256)
    description = models.TextField()
    location = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #         while Event.objects.filter(slug=self.slug).exists():
    #             self.slug = slugify(self.title) + '-' + str(random.randint(1, 9999))
    #     super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    fullname = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    date_of_birth = models.DateField(null=True)
    current_position = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=256, null=True)
    telegram = models.CharField(max_length=256, null=True)
    instagram = models.CharField(max_length=256, null=True)
    facebook = models.CharField(max_length=256, null=True)
    description = models.TextField(null=True)
    hours = models.FloatField(null=True)

    def __str__(self) -> str:
        return self.fullname


class Investor(models.Model):
    owner_image = models.ImageField()
    company_name = models.CharField(max_length=256)
    owner = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=15)
    INN = models.BigIntegerField()
    location = models.CharField(max_length=256)
    email = models.EmailField()
    website_url = models.URLField(null=True, blank=True)
    company_photos = models.ImageField()

    def __str__(self) -> str:
        return self.company_name


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name='title')
    image = models.ImageField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=256, null=True)

    def __str__(self) -> str:
        return self.title
