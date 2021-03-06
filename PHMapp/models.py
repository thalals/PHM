from django.db import models

# Create your models here.
class Order(models.Model) :
    image = models.ImageField(upload_to = 'images/')       #이미지
    price = models.IntegerField(default=0)
    customer = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    request = models.CharField(max_length=50)
    food = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


