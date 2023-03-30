from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = ('Categories')
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(null=False)
    image = models.ImageField(upload_to="images", blank=True)
    is_solid = models.BooleanField(default=False)
    createdBy = models.ForeignKey(
        User, related_name="items", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
