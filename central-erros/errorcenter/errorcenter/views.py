from django.shortcuts import render, redirect

from api.models import User
from api.views import UserToken
from errorcenter.forms import UserModelForm
from django.http import HttpResponse 

def user_login(request):
    if  request.method == 'POST':

        response = UserToken.post(request.POST, request.POST)
        status = response.status_code

        if (status != 200):
            return render(request, 'registration/login.html', {'error': response.data['error']})
        else:
            return redirect('/logs', {'token': response.data['token']})
    else:
        form = UserModelForm()

    context = {
        'form': form
    }
    return render(request, 'registration/login.html', {'form': form})