from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            #messages.success(request, 'Você esta logado(a)!') implementar depois
            return redirect('index')
        else:
            messages.error(request, 'Credenciais inválidas!')
            return redirect('login')

    else:
        return render(request, 'investor/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        #messages.success(request, 'Você deslogou!')
        return redirect('index')
