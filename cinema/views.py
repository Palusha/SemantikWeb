from rest_framework import generics

from .models import Actor
from .serializers import ActorSerializer


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
