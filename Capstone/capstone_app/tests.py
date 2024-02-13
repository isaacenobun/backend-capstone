from django.test import TestCase
from .models import menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .serializers import MenuSerializer

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        self.menu1 = menu.objects.create(Title="Bagel", Price=20, Inventory=9)

    def test_getall(self):
        # Make GET request to retrieve all Menu objects
        client = APIClient()
        url = reverse('menu')  # Assuming 'menu-list' is the URL name for the MenuViewSet
        response = client.get(url)

        # Check if the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the Menu objects
        expected_data = MenuSerializer([self.menu1], many=True).data

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, expected_data)