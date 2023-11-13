from django.urls import path

from . import views

urlpatterns = [
    path('<int:post_id>/', views.post, name='post'),
    path('', views.blog, name='blog'),
    path('exemplo/', views.exemplo, name='exemplo'),
]

