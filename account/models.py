from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group, Permission

class Account(AbstractBaseUser, PermissionsMixin):
    groups = models.ManyToManyField(Group, related_name='account_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='account_permissions', blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100,unique=True)
    area = models.TextField()
        
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "lastname"]


    class Meta:
        verbose_name =("Account")
        verbose_name_plural =("Accounts")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})
