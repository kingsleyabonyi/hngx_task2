from django.urls import path
from .views import add, update


urlpatterns = [
    path('', add, name='add'),
    path('/<int:pk>/', update, name='update')
]