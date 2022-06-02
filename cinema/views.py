from rest_framework import generics

from .models import Actor, Cinema, Employee, Food, Movie, Location
from .serializers import (
    ActorSerializer, CinemaSerializer, EmployeeSerializer,
    FoodSerializer, MovieSerializer, LocationSerializer
)


class ActorCreationView(generics.CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class ActorRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class ActorListView(generics.ListAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class ActorDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class CinemaCreationView(generics.CreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()


class CinemaRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()


class CinemaListView(generics.ListAPIView):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()


class CinemaDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()


class EmployeeCreationView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class MovieCreationView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class FoodCreationView(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class FoodRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class FoodListView(generics.ListAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class FoodDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class LocationCreationView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationListView(generics.ListAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
