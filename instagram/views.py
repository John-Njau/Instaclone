from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
def index(request):
    return render(request, 'registration/login.html')

@method_decorator(csrf_exempt, name = 'dispatch')
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(request):
        return redirect('home')

def home(request):
    return render(request, 'insta/home.html')

def logout(request):
    return render(request, '/')

def upload(request):
    return render(request, 'insta/upload.html')

def profile(request):
    return render(request, 'insta/profile.html')

def updateprofile(request):
    return render(request, 'insta/updateprofile.html')