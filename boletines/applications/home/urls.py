from django.urls import path

from .import views

app_name = "home_app"

urlpatterns = [
    #url pagina de inicio
    path(
        'panel/',
        views.HomePage.as_view(), 
        name = 'panel'
    )
]