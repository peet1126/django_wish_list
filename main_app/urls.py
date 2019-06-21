from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('wish/add', views.WishCreate.as_view(), name='wish_add'),
    path('wish/<int:pk>/delete/', views.WishDelete.as_view(), name='wish-delete'),
]