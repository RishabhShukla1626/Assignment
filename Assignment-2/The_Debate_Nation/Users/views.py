from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signupuser(request):
    if request.method == "GET":
        return render(request, 'Users/signupuser.html', {'form': CustomUserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                import pdb; pdb.set_trace()
                user = CustomUser.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('debates:debates')
            except Exception:
                return render(request, 'Users/signupuser.html', {'form': CustomUserCreationForm(), 'error':'The username has already been taken'})
        else:
            return render(request, 'Users/signupuser.html', {'form': CustomUserCreationForm(), 'error':'Password did not match'})


def loginuser(request):
    pass

def logoutuser(request):
    
    if request.method == "POST":
        logout(request)
        return redirect('signupuser')