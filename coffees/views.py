from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from utils.forms import DeleteConfirmForm
from .forms import CoffeeForm
from .models import Coffee


# Create your views here.
def index(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffees/index.html', {'coffees': coffees})


def show(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    return render(request, 'coffees/show.html', {'coffee': coffee})


def add(request):
    form = CoffeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功')
        return redirect('coffees:index')
    return render(request, 'coffees/add.html', {'form': form})


def edit(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    form = CoffeeForm(request.POST or None, instance=coffee)
    if form.is_valid():
        form.save()
        messages.success(request, '更新成功')
        return redirect('coffees:index')
    return render(request, 'coffees/edit.html', {'form': form})


def delete(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        coffee.delete()
        messages.success(request, '刪除成功')
        return redirect('coffees:index')
    return render(request, 'coffees/delete.html', {'form': form})
