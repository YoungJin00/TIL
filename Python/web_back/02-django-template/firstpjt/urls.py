from django.contrib import admin
from django.urls import path, include
# from articles import views
import articles, pages


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('articles/', views.index),
    # path('dinner/',views.dinner),
    # path('search/', views.search),
    # path('throw/', views.throw),
    # path('catch/', views.catch),
    # path('hello/<str:name>/', views.greeting),
    # path('articles/<int:num>/', views.detail),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
