from django.shortcuts import render, get_object_or_404
from .models import Guest

def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'tracker/guest_list.html', {'guests': guests})

def guest_detail(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    experiences = guest.experiences.all()
    reviews = guest.reviews.all()
    context = {
        'guest': guest,
        'experiences': experiences,
        'reviews': reviews,
    }
    return render(request, 'tracker/guest_detail.html', context)

def home(request):
    return render(request, 'tracker/home.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Guest
from .forms import GuestForm

def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'tracker/guest_list.html', {'guests': guests})

def guest_detail(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    return render(request, 'tracker/guest_detail.html', {'guest': guest})

def guest_create(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm()
    return render(request, 'tracker/guest_form.html', {'form': form})

def guest_update(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm(instance=guest)
    return render(request, 'tracker/guest_form.html', {'form': form})

def guest_delete(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        guest.delete()
        return redirect('guest_list')
    return render(request, 'tracker/guest_confirm_delete.html', {'guest': guest})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect('guest_list')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('guest_list')
    else:
        form = AuthenticationForm()
    return render(request, 'tracker/login.html', {'form': form})
