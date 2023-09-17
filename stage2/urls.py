from django.urls import path
from .views import ListCreatePerson, RetrieveUpdateDelete


urlpatterns = [
    path('', ListCreatePerson.as_view()),
    path('<int:pk>', RetrieveUpdateDelete.as_view())
]