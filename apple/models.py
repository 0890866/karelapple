from django.db import models

# Create your models here.

class AppleType(models.Model):
    apple_name = models.CharField(max_length=100)
    ripening_date = models.CharField(max_length=300, blank=True, default='-')
    eating = models.BooleanField()
    cooking = models.BooleanField()
    sauce = models.BooleanField()
    pie = models.BooleanField()
    juice = models.BooleanField()
    butter = models.BooleanField()
    notes = models.CharField(max_length=2000, blank=True, default='-')

    def __str__(self):
        return self.apple_name

class Recipe(models.Model):
    title = models.CharField(max_length=150)
    apple = models.ForeignKey(AppleType, on_delete=models.CASCADE, null=True)
    ingredients = models.TextField(blank=True)
    steps = models.TextField()
    author = models.CharField(max_length=50)
    picture = models.FileField()

