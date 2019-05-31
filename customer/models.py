from django.db import models

class Product(models.Model):
    """
    Product table to store the list of products that our Shipping Application
    is going to use
    """
    name = models.CharField(max_length=50)
    category = models.ManyToManyField('ProductCategory')
    availibility = models.BooleanField(default=False)
    price = models.FloatField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    """
    Category table to store the category of products offered by our Shipping Application
    This has a many to many relationship with Product table - One product can belong to multiple categories
    and one category can have multiple products
    """
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
