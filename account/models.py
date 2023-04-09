from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group, Permission
from .manager import AccoutManager
class Account(AbstractBaseUser, PermissionsMixin):
    groups = models.ManyToManyField(Group, related_name='account_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='account_permissions', blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100,unique=True)
    area = models.TextField()

    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "lastname"]


    objects = AccoutManager()

    def __str__(self):
        return str(self.first_name)

    def has_perm(self, perm, obj=None):
        return self.is_admin


    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"