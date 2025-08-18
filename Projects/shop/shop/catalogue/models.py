from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Tag(models.Model):
    name=models.CharField(max_length=28)


class Category(models.Model):
    name=models.CharField(max_length=28)
    tags=models.ManyToManyField(Tag,blank=True)

class Product(models.Model):  
    name=models.CharField(max_length=50)
    description=models.TextField()
    price=models.DecimalField(max_digits=4, decimal_places=2)
    stock=models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category=models.ForeignKey(Category, null=True,
    on_delete=models.PROTECT)
    tags=models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"Name: {self.name} Price:{self.price}"
    # return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart ({self.user.username})"

    def get_total_price(self):
        return sum(item.total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def total_price(self):
        return self.product.price * self.quantity