from django.urls import path,include
from . import views
from .views import BookingViewSet,UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('tables', BookingViewSet, 'booking')
router.register('users', UserViewSet, 'users')

urlpatterns = [
    # path('', views.home,  name='home'),
    path('', include(router.urls)),
    path('bookings/', views.bookings.as_view()),
    path('bookings/<int:pk>/',views.booking.as_view()),
    path('menu/', views.menuitems.as_view()),
    path('menu/<int:pk>/', views.menuitem.as_view()),
    path('message/', views.private),
    path('get-token/', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]+router.urls