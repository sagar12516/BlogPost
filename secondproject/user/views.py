from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'account created for the {username}!')
            return redirect('blog-home')

    else:
        form=RegisterForm()
    return render(request,'user/register.html',{'form':form})


@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            u_name=u_form.cleaned_data.get('username')
        messages.success(request,f'Your account has been updated {u_name}!')
        return redirect('user-profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={
    'u_form':u_form,
    'p_form':p_form
    }

    return render(request,'user/profile.html',context)
