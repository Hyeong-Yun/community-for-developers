from django.contrib import admin
from django.urls import path
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # html form을 이용하여 블로그 객체 만들기
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),

    # django formㅇ르 이용한 
    path('formcreate/', views.formcreate, name = 'formcreate'),

    # django modelform을 이용한 블ㅗ그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name = "modelformcreate")
]
