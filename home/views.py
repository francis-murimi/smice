from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from .models import Topitem
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm,UserProfileForm,LoginForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from orders.models import Order


def home(request):
    template = loader.get_template('home/home.html')
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'not logged in'
    items = Topitem.objects.all()[:9]
    context = {'username':username,'items':items}
    return HttpResponse(template.render(context,request))

def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect ('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            form = LoginForm()
    form = LoginForm()
    template = loader.get_template('home/login.html')
    context = {'form':form}
    return HttpResponse(template.render(context,request))

@login_required(login_url='/register/')
def profile(request):
    return render(request,'home/profile.html')

def register(request):
    template = loader.get_template('home/register.html')
    if request.method == 'POST':
        form =ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            
            profile.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()
    
    context = {'form':form,'profile_form':profile_form}
    return HttpResponse(template.render(context,request))

@login_required(login_url='/register/')
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('home')
    else:
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        u_form = UserUpdateForm(instance=request.user)

    context={'p_form': p_form, 'u_form': u_form}
    template = loader.get_template('home/update.html')
    return HttpResponse(template.render(context,request))

def log_out(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/register/')
def account(request):
    username = request.user.username
    context = {'username':username }
    template = loader.get_template('home/account.html')
    return HttpResponse(template.render(context,request))

@login_required(login_url='/register/')
def order_view(request):
    username = request.user.id
    orders = Order.objects.filter(orderer=username)
    paid_orders = Order.objects.filter(orderer=username,paid=True)
    unpaid_orders = Order.objects.filter(orderer=username,paid=False)
    context = {'orders':orders,'paid_orders':paid_orders,'unpaid_orders':unpaid_orders}
    template = loader.get_template('home/orders.html')
    return HttpResponse(template.render(context,request))

@login_required(login_url='/register/')
def order_see(request,id):
    order = get_object_or_404(Order,id=id)
    context = {'order':order }
    template = loader.get_template('home/order_see.html')
    return HttpResponse(template.render(context,request))

def documentation(request):
    template = loader.get_template('home/documentation.html')
    context = {}
    return HttpResponse(template.render(context,request))

def contact(request):
    template = loader.get_template('home/contact.html')
    context = {}
    return HttpResponse(template.render(context,request))