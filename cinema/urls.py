from django.urls import path

from . import views

app_name = 'cinema'

urlpatterns = [
    path('create-actor/', views.ActorCreationView.as_view(), name='actor-creation'),
    path('update-actor/<int:id>/', views.ActorUpdateView.as_view(), name='actor-update'),
    path('get-actor/<int:id>/', views.ActorRetrieveView.as_view(), name='actor-retrieve'),
    path('list-actor/', views.ActorListView.as_view(), name='actor-list'),
    path('delete-actor/<int:id>/', views.ActorDeleteView.as_view(), name='actor-delete')
]