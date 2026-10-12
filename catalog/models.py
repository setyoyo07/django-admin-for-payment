from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=23, decimal_places=2, default=0)
    is_active = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True, db_index=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"