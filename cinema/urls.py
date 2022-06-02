from django.urls import path

from . import views

app_name = 'cinema'

urlpatterns = [
    path('create-actor/', views.ActorCreationView.as_view(), name='actor-creation'),
    path('update-actor/<int:id>/', views.ActorUpdateView.as_view(), name='actor-update'),
    path('get-actor/<int:id>/', views.ActorRetrieveView.as_view(), name='actor-retrieve'),
    path('list-actor/', views.ActorListView.as_view(), name='actor-list'),
    path('delete-actor/<int:id>/', views.ActorDeleteView.as_view(), name='actor-delete'),
    path('create-cinema/', views.CinemaCreationView.as_view(), name='cinema-creation'),
    path('update-cinema/<int:id>/', views.CinemaUpdateView.as_view(), name='cinema-update'),
    path('get-cinema/<int:id>/', views.CinemaRetrieveView.as_view(), name='cinema-retrieve'),
    path('list-cinema/', views.CinemaListView.as_view(), name='cinema-list'),
    path('delete-cinema/<int:id>/', views.CinemaDeleteView.as_view(), name='cinema-delete'),
    path('create-employee/', views.EmployeeCreationView.as_view(), name='employee-creation'),
    path('update-employee/<int:id>/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('get-employee/<int:id>/', views.EmployeeRetrieveView.as_view(), name='employee-retrieve'),
    path('list-employee/', views.EmployeeListView.as_view(), name='employee-list'),
    path('delete-employee/<int:id>/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
    path('create-movie/', views.MovieCreationView.as_view(), name='movie-creation'),
    path('update-movie/<int:id>/', views.MovieUpdateView.as_view(), name='movie-update'),
    path('get-movie/<int:id>/', views.MovieRetrieveView.as_view(), name='movie-retrieve'),
    path('list-movie/', views.MovieListView.as_view(), name='movie-list'),
    path('delete-movie/<int:id>/', views.MovieDeleteView.as_view(), name='food-delete'),
    path('create-food/', views.FoodCreationView.as_view(), name='food-creation'),
    path('update-food/<int:id>/', views.FoodUpdateView.as_view(), name='food-update'),
    path('get-food/<int:id>/', views.FoodRetrieveView.as_view(), name='food-retrieve'),
    path('list-food/', views.FoodListView.as_view(), name='food-list'),
    path('delete-food/<int:id>/', views.FoodDeleteView.as_view(), name='food-delete'),
    path('create-location/', views.LocationCreationView.as_view(), name='location-creation'),
    path('update-location/<int:id>/', views.LocationUpdateView.as_view(), name='location-update'),
    path('get-location/<int:id>/', views.LocationRetrieveView.as_view(), name='location-retrieve'),
    path('list-location/', views.LocationListView.as_view(), name='location-list'),
    path('delete-location/<int:id>/', views.LocationDeleteView.as_view(), name='location-delete'),
]
