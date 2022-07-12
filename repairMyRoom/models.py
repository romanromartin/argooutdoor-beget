from django.db import models


class Complex(models.Model):
    complex = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.complex


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class Side(models.Model):
    side = models.CharField(max_length=200)

    def __str__(self):
        return self.side


class Repair(models.Model):
    repair = models.CharField(max_length=200)
    recat = models.ForeignKey(Category, on_delete=models.CASCADE)
    reside = models.ForeignKey(Side, on_delete=models.CASCADE)
    main = models.BooleanField(default=False)
    price = models.CharField(max_length=100)
    unit = models.CharField(max_length=60, default='-')

    def __str__(self):
        return self.repair

class Portfolio(models.Model):
    picture = models.ImageField(upload_to='static/portfolio', default='static/portfolio/default.webp')
    text = models.TextField(null=True)


class Call(models.Model):
    client = models.CharField(max_length=60, default='-')
    phone = models.CharField(max_length=10, default='-')
    date = models.DateTimeField()


































