from rest_framework import generics, status
from rest_framework.response import Response
from .models import Menu, Booking
from drf_spectacular.utils import extend_schema_view, extend_schema
from .serializers import MenuSerializer, BookingSerializer

# API views for Swagger documentation

# Class-based view for booking form submission with extended schema
@extend_schema_view(
    get=extend_schema(
        description="Get the booking data",
        responses={200: BookingSerializer(many=True)}
    ),
    post=extend_schema(
        description="Submit the booking form",
        request=BookingSerializer,
        responses={201: BookingSerializer}
    )
)
class BookingAPIView(generics.GenericAPIView):
    serializer_class = BookingSerializer

    def get(self, request, *args, **kwargs):
        # Fetch all booking objects from the database
        bookings = Booking.objects.all()
        # Serialize the booking data
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class-based view to list menu items with extended schema
@extend_schema_view(
    get=extend_schema(
        description="Get the list of menu items",
        responses={200: MenuSerializer(many=True)}
    )
)
class MenuListAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# Class-based view to retrieve a specific menu item
@extend_schema_view(
    get=extend_schema(
        description="Get a specific menu item by ID",
        responses={200: MenuSerializer, 404: "Menu item not found"}
    )
)
class MenuItemDetailAPIView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'pk'
