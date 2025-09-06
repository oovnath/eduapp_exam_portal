from django.contrib import admin
from django.urls import path
from django.contrib import admin
from courses import views

admin.site.site_header = "Education Portal"
admin.site.site_title = "Education portal | Dashboard"  # This changes the browser tab title
admin.site.index_title = "Education portal | Dashboard" # This is the main title on the index page

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.course_list, name='course_list'),
    path('create/', views.course_create, name='course_create'),
    path('update/<int:pk>/', views.course_update, name='course_update'),
    path('delete/<int:pk>/', views.course_delete, name='course_delete'),
]