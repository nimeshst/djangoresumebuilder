from django.shortcuts import render
from .forms import SignUpForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login

from django.http import HttpResponse
# Create your views here.


def signup(request):
    if request.method == "POST":

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('/UserDetails')
    else:
        form = SignUpForm()
        return render(request,"auth/signup.html",{'form':form})