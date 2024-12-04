from django.db import models

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Ошибка')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    company = models.CharField(_('Company'), max_length=30, blank=True)
    position = models.CharField(_('Position'), max_length=30, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

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

