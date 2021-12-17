from django.shortcuts import render
from .models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.db.models import Q
# Create your views here.

def events(request):
    query = ''
    today = datetime.datetime.today()
    if request.GET.get('search_query'):
        query = request.GET.get('search_query')
        events = Event.objects.exclude(published=False).filter(Q(start_date__gte=today) & 
        (Q(title__startswith=query) | Q(description__icontains=query))).order_by('-created')
    else:
        events = Event.objects.exclude(published=False).order_by('-created')    
    
    paginator = Paginator(events, 10)
    page = request.GET.get('page', 1)
    
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return render(request, 'home/events.html',{'events':events})

