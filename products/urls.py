from django.urls import path
from .views import landing_page, Info

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('info/', Info.as_view(), name='info'),
]