from django.db import models
from account.models import Account
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
class Repair(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Kvartera(models.Model):
    # STATUS = (
    #     ('ha','ha'),
    #     ('yuq','yuq'),
    # )
    # user = models.ForeignKey(Account,on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='kvartera')
    title = models.CharField(max_length=100)
    # category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    number_rooms = models.IntegerField()
    total_area = models.IntegerField()
    living_space = models.IntegerField()
    kitchen_area = models.PositiveIntegerField()
    floor = models.PositiveIntegerField()
    house_floor_plan = models.PositiveIntegerField()
    # year_of_construction = models.DateField()
    # furniture = models.CharField(max_length=50,choices=STATUS)
    # repair = models.ForeignKey(Repair,on_delete=models.CASCADE)
    # vositachilik_haqi = models.CharField(max_length=100,choices=STATUS)
    

    class Meta:
        verbose_name = ("kvartera")
        verbose_name_plural = ("kvarteras")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("kvartera_detail", kwargs={"pk": self.pk})
