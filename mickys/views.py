from django.shortcuts import render
from .models import UserProfile, Product
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForms, ProductForm
from django.shortcuts import redirect, get_object_or_404

from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'mickys/index.html')

@login_required()
def special(request):
    return HttpResponseRedirect('Logged in!')

@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


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


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Account not active')
        else:
            print('someone tried to login and failed')
            print('Username: {} and password {}'.format(username, password))

            return HttpResponse('invalid details')
    else:
        return render(request, 'mickys/login.html', {})



def get_product(request):
    all_product = Product.objects.all()
    context = {'all_product': all_product}

    return render(request, '', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('#product_home_page')

        else:
            form = ProductForm()
            context = {'form':form}
            return render(request, 'add_product_page', context)


def update_product(request):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Product page')

    else:
        form = ProductForm(instance=product)
        context = {'form':form}
        return render(request, 'update_product', context)


def delete(request):
    product = get_object_or_404(Product, pk=id)
    product.delete()

    return redirect('product page')



