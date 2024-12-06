from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django import forms



class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    class _meta:
        model = BaseUserManager

class User(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    company = models.CharField(('Company'), max_length=30, blank=True)
    position = models.CharField(('Position'), max_length=30, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'company', 'position']  # Можно добавить другие поля, если необходимо

    def clean_email(self):
        email = self.cleaned_data['email']
        # Проверка, что email уникален (исключая текущего пользователя)
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

class Contact(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             related_name='contacts', blank=True,
                             on_delete=models.CASCADE)

    city = models.CharField(max_length=40, verbose_name='Город')
    street = models.CharField(max_length=120, verbose_name='Улица')
    house = models.CharField(max_length=30, verbose_name='Дом', blank=True)
    structure = models.CharField(max_length=30, verbose_name='Корпус', blank=True)
    building = models.CharField(max_length=30, verbose_name='Строение', blank=True)
    apartment = models.CharField(max_length=30, verbose_name='Квартира', blank=True)
    phone = models.CharField(max_length=40, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Контакты пользователя'
        verbose_name_plural = "Список контактов пользователя"

    def __str__(self):
        return f'{self.city} {self.street} {self.house}'

