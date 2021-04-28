# from app.register.views import register_user
from django.conf.urls import url
# from .views import IndexView, LoginView, RegisterView, HomeView, ProductsView
from . import views
from .views import UserCreate

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/', views.LoginView.as_view(), name='login'),
    # url(r'^register/', views.RegisterView.as_view(), name='register'),
    url(r'^register/', UserCreate.as_view(), name='register'),
    url(r'^home/', views.HomeView.as_view(), name='home'),
    url(r'^products/', views.ProductsView.as_view(), name='products'),
]

