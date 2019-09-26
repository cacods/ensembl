import json

from django.urls import reverse
from rest_framework.test import APITestCase


class GengeAPITest(APITestCase):

    databases = {'default', 'remote'}

    def test_get_returns_right_entries(self):
        url = reverse('geneautocomplete-list', kwargs={
            'query': 'tmem18', 'species': 'danio_rerio', 'limit': 3
        })

        response = self.client.get(url)
        self.assertEqual(
            json.loads(response.content.decode('utf-8')),
            [
                {
                    "db": "core",
                    "display_label": "tmem18",
                    "location": "23:35642061-35649000",
                    "species": "danio_rerio",
                    "stable_id": "ENSDARG00000036704"
                },
                {
                    "db": "core",
                    "display_label": "tmem182a",
                    "location": "9:6915611-6927587",
                    "species": "danio_rerio",
                    "stable_id": "ENSDARG00000040374"
                },
                {
                    "db": "core",
                    "display_label": "tmem189",
                    "location": "8:28452738-28466870",
                    "species": "danio_rerio",
                    "stable_id": "ENSDARG00000042732"
                }
            ]
        )
