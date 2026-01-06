from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class AuthFlowTests(APITestCase):
    def test_register_returns_tokens(self):
        url = reverse("accounts:register")
        payload = {
            "username": "newuser",
            "email": "new@example.com",
            "password": "StrongPass123",
            "password2": "StrongPass123",
        }
        resp = self.client.post(url, payload, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertIn("tokens", resp.data)
        self.assertTrue(User.objects.filter(email="new@example.com").exists())

    def test_password_reset_flow(self):
        user = User.objects.create_user(
            username="demo", email="demo@example.com", password="OldPass123"
        )

        request_url = reverse("accounts:password-reset-request")
        resp_request = self.client.post(request_url, {"email": user.email}, format="json")
        self.assertEqual(resp_request.status_code, status.HTTP_200_OK)
        uid = resp_request.data["uid"]
        token = resp_request.data["token"]

        confirm_url = reverse("accounts:password-reset-confirm")
        resp_confirm = self.client.post(
            confirm_url,
            {
                "uid": uid,
                "token": token,
                "new_password": "NewPass456",
                "new_password2": "NewPass456",
            },
            format="json",
        )
        self.assertEqual(resp_confirm.status_code, status.HTTP_200_OK)

        user.refresh_from_db()
        self.assertTrue(user.check_password("NewPass456"))

