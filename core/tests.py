from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
# Create your tests here.


class TestListCreateResume(APITestCase):

    def resume_create_resume(self):
        sample_resume = {'name': "new", 'slug': "vintage"}
        response = self.client.post(reverse('create-resume'), sample_resume)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
