from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):
    def create_user(self, email: str, password: str) -> 'CustomUser':
        if not email:
            raise ValidationError('Email is required')
        email = self.normalize_email(email)
        password = make_password(password)
        user = self.model(email=email, password=password)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str) -> 'CustomUser':
        email = self.normalize_email(email)
        user = self.model(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user
    
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email',
        unique=True
    )
    is_active = models.BooleanField(
        verbose_name='Active',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='Staff',
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name='Superuser',
        default=False
    )
    date_joined = models.DateTimeField(
        verbose_name='Date joined',
        default=timezone.now
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_'):  # Проверка, не является ли пароль уже хэшированным
            self.password = make_password(self.password)
        super().save(*args, **kwargs)