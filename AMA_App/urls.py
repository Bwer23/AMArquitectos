from django.urls import include,path
from AMA_App import views


urlpatterns = [
    path('', views.index, name='index'),
]