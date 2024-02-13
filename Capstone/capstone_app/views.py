from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import menu,booking
from .serializers import BookingSerializer,MenuSerializer,UserSerializer

# Create your views here

# Pages
# ------------------------------------
def home(request):
    return render(request, 'index.html')


# Api Views
# Viewsets
# ------------------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated] 

class BookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] 

# Generics
# ------------------------------------
class bookings(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = booking.objects.all()
    serializer_class = BookingSerializer

class booking(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = booking.objects.all()
    serializer_class = BookingSerializer

class menuitems(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class menuitem(generics.RetrieveUpdateDestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

@api_view()
@permission_classes([IsAuthenticated])
def private(request):
    # Only authenticated users can see this view
    return Response({'msg':'Only Authenticated users can see this message'})