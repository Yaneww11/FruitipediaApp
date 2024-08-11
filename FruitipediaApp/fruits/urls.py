from django.urls import path, include
from FruitipediaApp.fruits import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-category/', views.create_category, name='create_category'),
    path('create-fruit', views.CreateFruitView.as_view(), name='create_fruit'),
    path('<int:pk>/', include([
        path('edit-fruit/', views.edit_view, name='edit_fruit'),
        path('delete-fruit/', views.delete_view, name='delete_fruit'),
        path('fruit-details/', views.details_view, name='fruit_details'),
    ]))
]
