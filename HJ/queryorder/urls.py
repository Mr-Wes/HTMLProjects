from django.urls import path
from . import views

app_name = 'queryorder'
urlpatterns = [
	path('main/', views.main),
]