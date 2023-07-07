from django.urls import path
from . import views
urlpatterns = [
    path('a/',views.index,name='index'),
    path('b/',views.index2,name='index2'),
]
