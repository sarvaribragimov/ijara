from django.db import models
from account.models import Account
from autoslug import AutoSlugField
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = AutoSlugField(populate_from='name', unique=True,max_length=100)
    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("post:post_list_view", args=[self.slug])



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
    image = models.ImageField(upload_to='kvartera')
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    number_rooms = models.IntegerField()
    total_area = models.IntegerField()
    living_space = models.IntegerField()
    kitchen_area = models.PositiveIntegerField()
    floor = models.PositiveIntegerField()
    house_floor_plan = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True, help_text="Is product available?")
    # year_of_construction = models.DateField()
    # furniture = models.CharField(max_length=50,choices=STATUS)
    # repair = models.ForeignKey(Repair,on_delete=models.CASCADE)
    # vositachilik_haqi = models.CharField(max_length=100,choices=STATUS)
    

    class Meta:
        verbose_name = ("kvartera")
        verbose_name_plural = ("kvarteras")

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("post:post_list_view", args=[self.category.slug, self.slug])

    def get_image_url(self):
        return self.image.url if self.image and hasattr(self.image, "url") else "#"

    # def get_absolute_url(self):
    #     return reverse("kvartera_detail", kwargs={"pk": self.pk})
