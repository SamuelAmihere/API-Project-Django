from django.db import models

# Create your models here.
class MarketCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.description


class Player(models.Model):
    name = models.CharField(max_length=250)
    market_type = models.ForeignKey(MarketCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=500,null=True)

    def __str__(self):
        return self.name
