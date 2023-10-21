from django.urls import path
from recipes.views import home


urlpatterns = [
    path('', home), #Home
    
    #exeplos de lincagem da url como a views
    #path('sobre/', sobre), #/sobre/ 
    #path('contato/', contato) #/contato/
]