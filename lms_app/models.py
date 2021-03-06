from django.db import models

# Create your models here.
class Categ(models.Model):
    Categ_title = models.CharField(max_length=50)
    def __str__(self):
        return self.Categ_title



class Book(models.Model):
    status_books = [
           ('available','available'),
           ('sold','sold'),
           ('rented','rented'),

    ]
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    status = models.CharField(max_length=50,choices=status_books,null=True,blank=True)
    photo_book = models.ImageField(upload_to='photos',null=True, blank=True)
    photo_author = models.ImageField(upload_to='photos',null=True, blank=True)
    pages = models.IntegerField(null=True, blank= True)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=True, blank= True)
    rental_price_day = models.DecimalField(max_digits=5,decimal_places=2,null=True, blank= True)
    rental_period = models.IntegerField(null=True, blank= True)
    active = models.BooleanField(default=True)
    Categ = models.ForeignKey(Categ ,on_delete=models.PROTECT)
  
    def __str__(self):
        return self.title
        