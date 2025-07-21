from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Quotes
from .forms import QuotesForm
import random, json


def index(request):
    allq = Quotes.objects.all()
    showone = random.choices(allq, weights = [q.weight for q in allq], k = 1)[0]
    showone.views += 1
    showone.save()
    return render(request, 'main/home.html', {'showone': showone})


def addquote(request):
    form = QuotesForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'main/addquote.html', {'form': form})


def showtop(request):
    top10 = Quotes.objects.order_by('-likes')[:10]
    return render(request, 'main/top.html', {'top10': top10})


@require_POST
def like(request, quote_id):
    quote = get_object_or_404(Quotes, id=quote_id)
    data = json.loads(request.body)
    remove = data.get("remove", False)
    if remove:
        quote.likes = max(0, quote.likes - 1)
    else:
        quote.likes += 1
    quote.save()
    return JsonResponse({"likes": quote.likes})

@require_POST
def dislike(request, quote_id):
    quote = get_object_or_404(Quotes, id=quote_id)
    data = json.loads(request.body)
    remove = data.get("remove", False)
    if remove:
        quote.dislikes = max(0, quote.dislikes - 1)
    else:
        quote.dislikes += 1
    quote.save()
    return JsonResponse({"dislikes": quote.dislikes})
