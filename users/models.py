from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

NULLABLE = {"blank": True, "null": True}


class UserManager(BaseUserManager):
    """
    Менеджер для создания пользователя через консоль
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Создание обычного пользователя
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создание суперпользователя
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Кастомная модель пользователя
    """
    email = models.EmailField(
        verbose_name="Email",
        unique=True,
        help_text="Укажите почту"
    )
    phone = models.CharField(
        verbose_name="Телефон",
        max_length=35,
        help_text="Укажите телефон", **NULLABLE
    )
    city = models.CharField(
        verbose_name="Город",
        max_length=35,
        help_text="Укажите город", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загрузите фото профиля",
        **NULLABLE,
    )
    tg_chat_id = models.CharField(
        verbose_name="ID чата в Телеграм",
        max_length=35,
        help_text="Укажите ID чата в Телеграм",
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
