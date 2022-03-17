from django.shortcuts import redirect, render

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.core.validators import validate_email

from accounts.models import FormContact


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=username, password=password)

    if not user:
        messages.error(request, 'Usuário ou senha inválido.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login efetuado com sucesso.')


def logout(request):
    auth.logout(request)
    return redirect('dashboard')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    name = request.POST.get('name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    name = request.POST.get('name')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    if not name or not last_name or not email or not username or not password or not confirm_password:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return render(request, 'accounts/register.html')

    if len(password) < 6:
        messages.error(request, 'Password precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/register.html')

    if password != confirm_password:
        messages.error(request, 'Password não conferem.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'User já existe.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe.')
        return render(request, 'accounts/register.html')

    messages.success(request, "Salvo")
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=name,
        last_name=last_name)

    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContact()
        return render(request, 'accounts/dashboard.html',{'form': form})

    form = FormContact(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário.')
        form = FormContact()
        return render(request, 'accounts/dashboard.html',{'form': form})

    description = request.POST.get('description')

    if len(description) < 5:
        messages.error(request, 'Descrição precisa ter mais de 5 caracteres.')
        form = FormContact()
        return render(request, 'accounts/dashboard.html',{'form': form})

    form.save()
    messages.success(request, f'Contato {request.POST.get("name")} salvo com sucesso! ')
    return redirect('dashboard')