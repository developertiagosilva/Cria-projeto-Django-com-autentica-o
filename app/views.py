from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# def index(request):
#     return render(request, 'app/index.html')

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario_autenticado = authenticate(
            request,
            username = username,
            password = password,
        )

        if usuario_autenticado is not None:
            login(request, usuario_autenticado)
            return redirect("painel")

        return render(
            request, 
            "app/index.html",
            {"erro": "Usuario ou senha inválida."}
        )
    return render(request, "app/index.html")

def sair(request):
    logout(request)
    return redirect("index")

@login_required
def painel(request):
    return render(request, "app/painel.html")