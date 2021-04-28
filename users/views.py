from django.views.generic.edit import CreateView
from .models import Users
from django.conf.urls import reverse_lazy

class UserCreate(CreateView):
    model = Users
    fields = [
        'name', 'login', 'password', 'cep', 'address',
        'number', 'complement', 'district', 'city', 'state'
    ]
    template_name = 'register.html'
    success_url = reverse_lazy('login')
