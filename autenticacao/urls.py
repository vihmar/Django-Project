from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.signup, name='signup'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('consulta/', views.plataforma, name='consulta')
]