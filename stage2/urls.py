from django.urls import path
from .views import ListCreatePerson, RetrieveUpdateDeletePerson


urlpatterns = [
    path('', ListCreatePerson.as_view()),
    path('<int:pk>', RetrieveUpdateDeletePerson.as_view())
]