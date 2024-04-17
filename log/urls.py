from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistrationAPIView, LoginAPIView, LogoutAPIView, StaffViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'staff', StaffViewSet, basename='staff')



# The API URLs are now determined automatically by the router.
urlpatterns = [
   path('', include(router.urls)),
   path('register/', RegistrationAPIView.as_view(), name='user-registration'),
   path('login/', LoginAPIView.as_view(), name='user-login'),
   path('logout/', LogoutAPIView.as_view(), name='user-logout'),
]