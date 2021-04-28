from django.conf.urls import url
from .views import UserCreate

urlpatterns = [
    url(r'^', UserCreate.as_view(), name='register-user')
]
