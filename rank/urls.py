from django.urls import path
from . import views

urlpatterns = [
    path('', views.uploadCsv,name='upload_csv'),
    path('overview/',views.overview,name='overview'),
    path('match-delete/<int:match_id>/',views.delete,name='delete_match'),
    path('edit/<int:match_id>/', views.edit, name='edit_match'),
    path('matches/', views.match_list, name='match_list'),
]

