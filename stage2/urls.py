from django.urls import path
from .views import add, update


urlpatterns = [
    path('', add, name='add'),
    path('user_id/<int:pk>/', update, name='update')
]