from django.shortcuts import render, redirect
from .models import Quotedatabase
from .forms import QuotesdatabaseForm
import random

def index(request):
    allq = Quotedatabase.objects.all()
    showone = random.choices(allq, weights = [q.weight for q in allq], k = 1)[0]
    return render(request, 'main/home.html', {'showone': showone})

def addquote(request):
    if request.method == 'POST':
        form = QuotesdatabaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = QuotesdatabaseForm()
    return render(request, 'main/addquote.html', {'form': form})

def showtop(request):
    top10 = Quotedatabase.objects.order_by('-likes')[:10]
    return render(request, 'main/top.html', {'top10': top10})