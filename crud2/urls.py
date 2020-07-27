from django.urls import path
from . import views

app_name = 'crud2'

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
]
