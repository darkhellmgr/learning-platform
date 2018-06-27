from django.urls import path
from user import views

urlpatterns = [
    path('sign/', views.sign, name='signin'),
    path('postsign/', views.postsign, name='welcome'),
    path('logout/', views.logout, name="log"),
    path('signup/', views.signup, name="signup"),
    path('postsignup/', views.postsignup, name='postsignup'),
]
