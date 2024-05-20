import logging
import random
from json import JSONDecodeError

import django_filters
from django.db.models.expressions import Case, When
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, views, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Restaurant, Review, User
from .serializers import (
    RestaurantWithDistrictAndCategoriesSerializer,
    ReviewSerializer,
    ReviewWithRestaurantSerializer,
    UserSerializer,
)

logger = logging.getLogger(__name__)


class RestaurantFilterSet(django_filters.FilterSet):
    class Meta:
        model = Restaurant
        fields = ["district__name", "categories__name"]


# restaurant recommendation
class UserRestaurantViewSet(ListModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    filter_backends = [DjangoFilterBackend]
    filter_class = RestaurantFilterSet
    permission_classes = (IsAuthenticated,)
    serializer_class = RestaurantWithDistrictAndCategoriesSerializer

    def get_queryset(self):
        import recommender_models.recommender

        user_id = int(self.kwargs["user_pk"])
        visited_restaurant_ids = tuple(
            review.restaurant_id for review in Review.objects.filter(user=user_id)
        )

        recommendations = list(
            recommender_models.recommender.recommend(
                user_id,
                blacklist=visited_restaurant_ids,
                randomized=False,
            )
        )

        random.shuffle(recommendations)

        # logger.info(
        #     "recommend %s for user %s, who has visited %s",
        #     recommendations,
        #     user_id,
        #     visited_restaurant_ids,
        # )
        ids = [int(r[2]) for r in recommendations]
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
        return (
            Restaurant.objects.prefetch_related("categories")
            .prefetch_related("district")
            .filter(pk__in=ids)
            .order_by(preserved)
        )


class UserViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_serializer_class(self):
    #     if self.action == "retrieve":
    #         return UserWithReviewsSerializer
    #     return UserSerializer

    @action(
        methods=["get"],
        detail=True,
    )
    def reviews(self, request, pk=None):
        return Response(
            ReviewWithRestaurantSerializer(
                Review.objects.prefetch_related("restaurant")
                .filter(user=pk)
                .order_by("-review_date")[:100],
                many=True,
            ).data
        )


class ReviewAPIView(views.APIView):
    """
    A simple APIView for creating review entires.
    """

    serializer_class = ReviewSerializer

    def get_serializer_context(self):
        return {"request": self.request, "format": self.format_kwarg, "view": self}

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = ReviewSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse(
                {"result": "error", "message": "Json decoding error"}, status=400
            )
