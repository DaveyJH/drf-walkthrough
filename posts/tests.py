from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username="test user", password="test_pass")

    def test_can_list_posts(self):
        user = User.objects.get(username="test user")
        Post.objects.create(owner=user, title="test post")
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data[0]["title"], "test post")

    def test_logged_in_user_can_create_post(self):
        self.client.login(username="test user", password="test_pass")
        response = self.client.post("/posts/", {"title": "test post"})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_post(self):
        response = self.client.post("/posts/", {"title": "test post"})
        count = Post.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username="test user", password="test_pass")
        other = User.objects.create_user(
            username="other user",
            password="other_pass"
        )
        Post.objects.create(owner=other, title="other post")

    def test_can_view_specific_post(self):
        response = self.client.get("/posts/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "other post")

    def test_cannot_view_non_existent_post(self):
        response = self.client.get("/posts/99/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_update_owned_post(self):
        self.client.login(username="test user", password="test_pass")
        self.client.post("/posts/", {"title": "test post"})
        response = self.client.put("/posts/2/", {"title": "edited post"})
        self.assertEqual(response.data["title"], "edited post")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_cannot_update_other_post(self):
        self.client.login(username="test user", password="test_pass")
        response = self.client.put("/posts/1/", {"title": "edited post"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_out_user_cannot_update_post(self):
        response = self.client.put("/posts/1/", {"title": "test post"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
