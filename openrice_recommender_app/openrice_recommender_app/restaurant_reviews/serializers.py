from rest_framework import serializers

from . import models


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class RestaurantWithDistrictAndCategoriesSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = models.Restaurant
        fields = "__all__"


class ReviewWithRestaurantSerializer(serializers.ModelSerializer):
    restaurant = RestaurantWithDistrictAndCategoriesSerializer(read_only=True)

    class Meta:
        model = models.Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = "__all__"
        # fields = (
        #     "id",
        #     "rating_taste",
        #     "rating_decor",
        #     "rating_service",
        #     "rating_hygiene",
        #     "rating_value",
        #     "dining_method",
        #     "review_date",
        #     "date_of_visit",
        #     "spending_per_head",
        #     "title",
        #     "comment",
        #     "restaurant",
        #     "user",
        # )


class UserWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewWithRestaurantSerializer(many=True, read_only=True)

    class Meta:
        model = models.User
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"
