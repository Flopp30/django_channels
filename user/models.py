from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True


class User(PermissionsMixin, AbstractBaseUser):
    id = models.UUIDField(verbose_name="id", primary_key=True)
    username = models.CharField(verbose_name="username", max_length=128, unique=True)
    USERNAME_FIELD = "username"
    objects: UserManager = UserManager()

    def __str__(self):
        return f"{self.id}: {self.username}"

    def __repr__(self):
        return f"User(username={self.username})"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
