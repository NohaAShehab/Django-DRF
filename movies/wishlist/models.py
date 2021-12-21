from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return f"{self.name}"


class WishList(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE,
                                 null=True, related_name="wishlist")

    def __str__(self):
        return f"{self.title}"


class Reviews(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(5)])
    description = models.CharField(max_length=100, null=True)
    active = models.BooleanField(null=True)
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE,
                                 null=True, related_name="reviews")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rating} {self.wishlist}"
