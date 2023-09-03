from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import Edit_profile_form, User_Profile_Form





def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'user/register.html', {'form': form})



            
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')      



def login_view(request):
    if request.method == 'POST':
       
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            
            login(request, user)
            return redirect('home')  
        else:
         
            error_message = 'Invalid username or password'

    else:
        error_message = None

    return render(request, 'user/login.html', {'error_message': error_message})





@login_required
def edit_profile_view(request):
    user_profile = request.user.user_profile  
    if request.method == 'POST':
        user_form = Edit_profile_form(request.POST, instance=request.user)
        profile_form = User_Profile_Form(request.POST, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('edit_profile')  
    else:
        user_form = Edit_profile_form(instance=request.user)
        profile_form = User_Profile_Form(instance=user_profile)

    return render(request, 'user/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})





