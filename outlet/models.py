from django.db import models

# Create your models here.
class Product(models.Model):
    product_name= models.CharField(max_length=50)
    category= models.CharField(max_length=50, default='')
    subcategory= models.CharField(max_length=50, default='')
    price= models.IntegerField(default=0)
    desc= models.CharField(max_length=200, default='')
    pub_date= models.DateField(auto_now_add=True)
    image= models.ImageField(upload_to='outlet/images', default='')

    def __str__(self):
        return self.product_name