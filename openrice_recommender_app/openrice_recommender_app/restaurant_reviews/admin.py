from django.contrib import admin
from restaurant_reviews.models import Category, District, Restaurant, Review, User

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(District)
admin.site.register(Restaurant)
admin.site.register(Review)

# alternative way to register a Model to admin
# @admin.register(Category)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
