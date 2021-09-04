from django.urls import path

from . import views

app_name = "Index_App"

urlpatterns = [
    path('', views.IndexView.as_view(), name="Index"),
    path('User/NuevaPublicacion/', views.NewPublicacionView.as_view(), name='nueva_publicacion'),
    path('User/MisPublicaciones/', views.UserPubView.as_view(), name="user-publicaciones"),
    path('User/EditarPublicacion/<pk>/', views.PublicacionUpdateView.as_view(), name='editar_publicacion'),
    path('User/EliminarPublicacion/<pk>/', views.PublicacionDeleteView.as_view(), name='eliminar_publicacion'),
]
