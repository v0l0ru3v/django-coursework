from django.shortcuts import render
from django.views import View
from users.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.shortcuts import redirect

class Register(View):
    template_name = 'registration/register.html'

    def get(self,request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context) 
    
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
# Create your views here.
