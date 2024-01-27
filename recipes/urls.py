from django.urls import path
from . import views #O ponto indica a pasta que você esta no caso é 'recipes'


urlpatterns = [
    path('', views.home), 
    path('recipes/<int:id>/', views.recipe),
]