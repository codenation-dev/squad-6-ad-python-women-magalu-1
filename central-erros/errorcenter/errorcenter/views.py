from django.shortcuts import render, redirect

from api.models import User
from errorcenter.forms import UserModelForm

def user_login(request):
    if  request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            #return redirect('')
    else:
        form = UserModelForm()

    context = {
        'form': form
    }
    return render(request, 'registration/login.html', {'form': form}) 