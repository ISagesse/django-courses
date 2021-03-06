from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('<int:id>', views.check),
    path('<int:id>/delete', views.delete)
]