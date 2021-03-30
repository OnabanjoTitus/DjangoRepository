from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello_world, name='hello'),
    path('five', views.fiver, name='five')

]
