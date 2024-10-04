from django.urls import path
from . import views

urlpatterns = [
    # HTML views (not part of the API documentation)
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),

    # API views for Swagger documentation
    path('api/bookings/', views.BookingAPIView.as_view(), name="api_bookings"),
    path('api/menu/', views.MenuListAPIView.as_view(), name="api_menu"),
    path('api/menu_item/<int:pk>/', views.MenuItemDetailAPIView.as_view(), name="api_menu_item"),
]
