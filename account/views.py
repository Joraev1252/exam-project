from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from account.forms import RegisterForm, AccountAuthenticationForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            full_name = form.cleaned_data.get('full_name')
            raw_password = form.cleaned_data.get('password1')

            account = authenticate(email=email, full_name=full_name, password=raw_password)
            login(request, account)
            if request.user.is_superuser:
                return redirect('report:vc_report')
            else:
                return redirect('report:report')
        else:
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form
    return render(request, 'sign_up.html', context)


def authentication(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if request.user.is_superuser:
            return redirect('report:vc_report')
        else:
            return redirect('report:report')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                if request.user.is_superuser:
                    return redirect('report:vc_report')
                else:
                    return redirect('report:report')


    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'sign_in.html', context)


def signout_view(request):
    logout(request)
    return redirect('account:signin')
