from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        # Create a minimal valid JPEG file for testing
        cls.test_image = SimpleUploadedFile(
            name="test_project.jpg",
            content=b"\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00",
            content_type="image/jpeg",
        )

        cls.post = Post.objects.create(
            title="a good title",
            body="nice body content",
            author=cls.user,
            image=cls.test_image,  # ✅ Attach test image
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "a good title")
        self.assertEqual(self.post.body, "nice body content")
        self.assertEqual(self.post.author.username, "testuser")

    def test_post_has_image(self):
        """Verify the image field is populated and returns a valid URL."""
        self.assertTrue(self.post.image)
        self.assertIn("test_project", self.post.image.url)
        self.assertTrue(self.post.image.url.endswith(".jpg"))

    def test_url_exists(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_project_details(self):
        response = self.client.get(
            reverse("project_details", kwargs={"pk": self.post.pk})
        )
        no_response = self.client.get("/projects/100/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "a good title")
        self.assertTemplateUsed(response, "project_details.html")

    def test_project_detail_shows_image(self):
        """Verify the project detail page renders the uploaded image."""
        response = self.client.get(
            reverse("project_details", kwargs={"pk": self.post.pk})
        )
        self.assertEqual(response.status_code, 200)
        # Check that the image URL appears in the rendered HTML
        self.assertContains(response, self.post.image.url)
