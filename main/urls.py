from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
	
	path('', views.index, name="home"),
	path('results', views.results, name="results"),
        path('detail/<int:id>/', views.detail, name='detail'),

	]
