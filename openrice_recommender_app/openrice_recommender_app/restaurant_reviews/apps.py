from django.apps import AppConfig


class RestaurantReviewsConfig(AppConfig):
    name = "restaurant_reviews"

    def ready(self):
        # kick start the signal receiver on app bootup
        import restaurant_reviews.signals
