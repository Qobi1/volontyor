from django.core.validators import EmailValidator
from django.db import models
from django.utils.text import slugify
import random
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=20)


class Event(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Event.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.title) + '-' + str(random.randint(1, 9999))
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
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
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self) -> str:
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
            while Volunteer.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.fullname) + '-' + str(random.randint(1, 9999))
        super().save(*args, **kwargs)


class Investor(models.Model):
    image = models.ImageField()
    company_name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.company_name)
            # Ensure the generated slug is unique
            while Investor.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.company_name) + '-' + str(random.randint(1, 9999))
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.company_name


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name='title')
    image = models.ImageField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=256, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # Ensure the generated slug is unique
            while News.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.title) + '-' + str(random.randint(1, 9999))
        super().save(*args, **kwargs)
