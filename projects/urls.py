from django.urls import path, re_path
from . import views

urlpatterns = [
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('', views.index, name='index'),
    path('CV', views.CV, name ='CV'),
    path('About', views.about, name='About'),
    path('technology/<str:technology>/', views.tech_projects, name='tech_projects')
]