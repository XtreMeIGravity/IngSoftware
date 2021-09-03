from django.urls import path

from . import views

app_name = "Index_App"

urlpatterns = [
    path('', views.IndexView.as_view(), name="Index"),
    path('NuevaPublicacion/', views.NewPublicacionView.as_view(), name='nueva_publicacion'),
]
