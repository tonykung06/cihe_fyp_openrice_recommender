import datetime
from turtle import title

from django.db import models


class User(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    user_level = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name}"


class District(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name}"


class Category(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    category_type_id = models.PositiveIntegerField()
    category_type_key = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name}"


class Restaurant(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image_url = models.URLField(max_length=500)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category, related_name="restaurants")

    def __str__(self) -> str:
        return f"{self.name} ({self.district.name if self.district else 'Unknown'})"


class Review(models.Model):
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        Restaurant, related_name="reviews", on_delete=models.CASCADE
    )
    rating_taste = models.PositiveIntegerField()
    rating_decor = models.PositiveIntegerField()
    rating_service = models.PositiveIntegerField()
    rating_hygiene = models.PositiveIntegerField()
    rating_value = models.PositiveIntegerField()
    dining_method = models.CharField(max_length=200)
    review_date = models.DateField(null=True)
    date_of_visit = models.DateField(null=True)
    spending_per_head = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.name} reviewed {self.restaurant.name} on {self.review_date}"
