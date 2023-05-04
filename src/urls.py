from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # (R) READ
    path('', views.Read.as_view(),name="read"),
    # (C) CREATE
    path('create/', views.Create.as_view(),name="create"),
    # (U) UPDATE
    path('update/<int:pk>/', views.Update.as_view(),name="update"),
    # (D) DELETE
    path('delete/<int:pk>/', views.Delete.as_view(),name="delete"),
]
