from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm
from .models import Userprofile

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('tree')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)




def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/order/checkout/')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)

def refer_view(request):
    if request.method == 'POST':
        if 'fn' in request.POST:
            up = Userprofile()
            up.productinfo = request.POST['pdi']
            up.First_name = request.POST['fn']
            up.Address1 = request.POST['ad1']
            up.Address2 = request.POST['ad2']
            up.website = request.POST['city']
            up.goals_for_digital_marketing = request.POST['phone']
            up.txnid = request.POST['txid']
            up.discount = request.POST['dis']
            up.net_amount_debit = request.POST['net']
            up.username = request.user
            up.refer = request.POST['refer']
            if up.no_of_referals == 2:
                var= "this user has already maximun no of referals please try again with another refer id"
            else:
                up.save()
                us=Userprofile.objects.get(username=up.refer)
                us.no_of_referals+=1
                us.save()
                data = up
    context = {
        'data': data,
        'var':var
    }
    return render(request, "myprofile.html", context)



def logout_view(request):
    logout(request)
    return redirect('/')
