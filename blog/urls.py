from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello_world),
    path('get-selected/', views.get_selected, name="get-selected"),
    path('search-content/', views.search_content, name="search-content"),
]
