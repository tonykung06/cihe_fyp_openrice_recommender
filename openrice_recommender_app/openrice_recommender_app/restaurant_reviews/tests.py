from django.contrib.auth.models import User as AuthUser
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from .models import Restaurant, Review, User


class UserTestCase(APITestCase):
    """
    Test suite for User
    """

    def setUp(self):
        User.objects.create(
            id=1,
            name="test user",
            user_level="test level",
        )
        User.objects.create(
            id=2,
            name="test user 2",
            user_level="test level",
        )
        self.users = User.objects.all()
        self.auth_user = AuthUser.objects.create_user(
            username="testuser1", password="this_is_a_test", email="testuser1@test.com"
        )

        # The app uses token authentication
        self.token = Token.objects.get(user=self.auth_user)
        self.client = APIClient()

        # We pass the token in all calls to the API
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_get_all_users(self):
        """
        test ItemsViewSet list method
        """
        self.assertEqual(self.users.count(), 2)
        response = self.client.get("/user/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_item(self):
        """
        test ItemsViewSet retrieve method
        """
        for user in self.users:
            response = self.client.get(f"/user/{user.id}/")
            self.assertEqual(response.status_code, status.HTTP_200_OK)


class ContactTestCase(APITestCase):
    """
    Test suite for Contact
    """

    def setUp(self):
        self.client = APIClient()
        User(id=84390, name="test user", user_level="test level").save()
        Restaurant(
            id=12744,
            name="test restaurant",
            address="test address",
            image_url="test url",
        ).save()

        self.data = {
            "rating_taste": 4,
            "rating_decor": 2,
            "rating_service": 2,
            "rating_hygiene": 2,
            "rating_value": 4,
            "dining_method": "omg",
            "review_date": "2009-01-09",
            "date_of_visit": None,
            "spending_per_head": "$10 (Tea)",
            "title": "test title",
            "comment": "test comment",
            "restaurant": 12744,
            "user": 84390,
        }
        self.url = "/review/"

    def test_create_review(self):
        """
        test ContactViewSet create method
        """
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(Review.objects.get().title, "test title")

    def test_create_review_without_title(self):
        """
        test ContactViewSet create method when title is not in data
        """
        data = self.data
        data.pop("title")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_review_when_title_equals_blank(self):
        """
        test ContactViewSet create method when title is blank
        """
        data = self.data
        data["title"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_review_without_comment(self):
        """
        test ContactViewSet create method when comment is not in data
        """
        data = self.data
        data.pop("comment")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_review_when_comment_equals_blank(self):
        """
        test ContactViewSet create method when comment is blank
        """
        data = self.data
        data["comment"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_review_without_dining_method(self):
        """
        test ContactViewSet create method when dining_method is not in data
        """
        data = self.data
        data.pop("dining_method")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_review_when_review_date_equals_blank(self):
        """
        test ContactViewSet create method when review_date is blank
        """
        data = self.data
        data["review_date"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_review_when_review_date_equals_non_review_date(self):
        """
        test ContactViewSet create method when review_date is not review_date
        """
        data = self.data
        data["review_date"] = "test"
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
