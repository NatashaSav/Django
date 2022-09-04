from django.urls import path
from calculator.views import recipe

urlpatterns = [

    path('<current_recept>/', recipe, name='omlet')
]
