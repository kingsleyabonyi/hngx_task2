from django.urls import path
from .views import add, update, get_person


urlpatterns = [
    path('', add, name='add'),
    path('/<int:pk>/', update, name='update'),
    path('get_person/<int:pk>/',get_person, name='get_person')
]