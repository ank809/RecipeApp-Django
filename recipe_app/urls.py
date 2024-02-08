from django.urls import path
from . import views
urlpatterns=[
    path('form/',views.form ),
    path('view_recipes/', views.view_recipe),
    path('delete-recipe/<id>/', views.delete_recipe),
    path('update_recipe/<id>/', views.update_recipe),
]   