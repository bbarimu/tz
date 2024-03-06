from . import views
from django.urls import path

urlpatterns = [
    path('recipes/', views.ReceptListView.as_view()),
    path('recipes/<int:pk>/', views.ReceptDetailView.as_view()),
    path('recipes/<int:pk>/update', views.ReceptUpdateView.as_view()),
    path('recipes/<int:pk>/delete', views.ReceptDeleteView.as_view()),
    path('recipes/create', views.ReceptCreateView.as_view())
]