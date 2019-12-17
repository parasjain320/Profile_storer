from django.urls import path
from django.conf.urls import  url
#from .views import HomePageView
from .import views

urlpatterns=[
    path('', views.home, name='company-home'),
    path('register/', views.register, name='company-register'),
    path('member_list/', views.member_list, name='company-list'),
    path('login/', views.login, name='company-login'),
    path('add/', views.add, name='company-add'),
    path('<int:id>', views.member_detail, name='detail'),
    path('<int:id>/edit', views.member_update, name='update'),
    # path('detail/<int:pk>', views.detail, name='company-detail'),
    # path('edit_profile/<int:pk>', views.edit_profile, name='company-edit'),


]
