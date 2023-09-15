from django.urls import path
from .views import add, update


urlpatterns = [
    path('add/', add, name='add'),
    path('update/<int:pk>/', update, name='update')
]