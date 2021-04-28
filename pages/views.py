# from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Users
from django.core.urlresolvers import reverse_lazy
# from django.urls import reverse_lazy
# from django.contrib.auth.models import User
# from django.views.decorators.http import require_POST


class IndexView(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class UserCreate(CreateView):
    model = Users
    fields = [
        'name', 'login', 'password', 'address', 'complement', 'district', 'city', 'state'
        #, 'number', 'cep'
    ]
    template_name = 'register.html'
    success_url = reverse_lazy('login')

# class RegisterView(TemplateView):
#     template_name = 'register.html'
#     @require_POST
#     def register_user(request):
#         name = request.POST['name']
#         email = request.POST['email']
#         password = request.POST['password']
#         cep = request.POST['cep']
#         address = request.POST['address']
#         number = request.POST['number']
#         complement = request.POST['complement']
#         district = request.POST['district']
#         city = request.POST['city']
#         state = request.POST['state']

#         newUser = User.objects.create_user(
#             name = name,
#             email = email,
#             password = password,
#             cep = cep,
#             address = address,
#             number = number,
#             complement = complement,
#             district = district,
#             city = city,
#             state = state,
#         )
#         newUser.save()

class HomeView(TemplateView):
    template_name = 'home.html'

class ProductsView(TemplateView):
    template_name = 'products.html'
