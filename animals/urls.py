from django.urls import path
from .views import AnimalView, AnimalViewById

urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('animals/<int:animal_id>/', AnimalViewById.as_view())
]