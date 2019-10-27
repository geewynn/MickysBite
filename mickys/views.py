from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForms


# Create your views here.

def index(request):
    return render(request, 'mickys/index.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_profile = UserProfileForms(data=request.POST)

        if user_form.is_valid() and user_profile.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print(user_form.errors, user_profile.errors)
    else:
        user_form = UserForm()
        user_profile = UserProfileForms()

#    context ={'user_form': user_form, 'user_profile':user_profile, 'registered':registered}

    return render(request, 'mickys/registration.html',
                  {'user_form': user_form, 'user_profile':user_profile, 'registered':registered})

