
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import diagnosis
from django.contrib.auth.models import User

class SaveConfidenceAPITest(TestCase):
    def setUp(self):
        
        self.user = User.objects.create(username="testuser")

        
        self.diag = diagnosis.objects.create(
            diagID=1,
            confidence=0,
            userID=self.user  
        )

    def test_valid_confidence(self):
        response = self.client.post(
            reverse('saveConfidence', args=[self.diag.diagID]),
            {'confidence': 85},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.diag.refresh_from_db()
        self.assertEqual(self.diag.confidence, 85)

    def test_invalid_confidence(self):
        response = self.client.post(
            reverse('saveConfidence', args=[self.diag.diagID]),
            {'confidence': 150},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# Create your tests here.
