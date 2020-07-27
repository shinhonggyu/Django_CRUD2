from django.urls import path
from . import views

app_name = 'crud2'

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
]
