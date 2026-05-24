from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id}"


class CartItem(models.Model):

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name


class Category(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    
class Store(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True

    )

    location = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="Calgary"
    )
    logo = models.ImageField(
        upload_to='store_logos/',
        blank=True,
        null=True
    )

    address = models.CharField(
        max_length=255, 
        blank=True,
        null=True   )

    website = models.URLField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):

    UNIT_CHOICES = [
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('l', 'Litre'),
        ('ml', 'Millilitre'),
        ('pcs', 'Pieces'),
    ]

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(
        max_length=255
    )

    quantity = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )

    unit = models.CharField(
        max_length=10,
        choices=UNIT_CHOICES,
        default='pcs'
    )

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    def __str__(self):

        return (
            f"{self.name} "
            f"({self.quantity} {self.unit})"
        )
class Price(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="prices"
    )

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="prices"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    scraped_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ("product", "store")

    def __str__(self):

        return (
            f"{self.product.name} - "
            f"{self.store.name} - "
            f"${self.price}"
        )