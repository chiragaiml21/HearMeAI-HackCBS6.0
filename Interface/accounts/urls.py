from django.urls import path

from . import views

urlpatterns = [
    path('start-learning', views.register_username, name='register-username'),
    path('add-age', views.register_age, name='register-age'),
    path('one-last-step', views.register_avatar, name='register-avatar'),  
    
    path("success", views.success, name="success"),
    
    path("lets-go", views.login, name="login"),
    path("check_bandwidth", views.check_bandwidth, name="check_bandwidth"),
    path("logout", views.logout, name="logout")
]
