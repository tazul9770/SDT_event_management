from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.timezone import now
from django.db.models import Count, Q
from event.models import Event
from event.forms import EventCreateForm
from django.contrib.auth.decorators import login_required

def dashboard(request):
    today = now().date()
    dates = request.GET.get('dates')

    counts = Event.objects.aggregate(
        total_events = Count('id'),
        todays_events = Count('id', filter=Q(date=today)),
        upcoming_events = Count('id', filter=Q(date__gt=today)),
        past_events = Count('id', filter=Q(date__lt=today))
    )

    base_query = Event.objects.select_related('category').prefetch_related('participant')

    if dates == 'todays':
        events = base_query.filter(date=today)
    elif dates == 'upcoming':
        events = base_query.filter(date__gt=today)
    elif dates == 'past':
        events = base_query.filter(date__lt=today)
    else:
        events = Event.objects.select_related('category').prefetch_related('participant').all()

    context = {
        'total_events':counts['total_events'],
        'todays_events':counts['todays_events'],
        'upcoming_events':counts['upcoming_events'],
        'past_events':counts['past_events'],
        'events':events
    }
    return render(request, 'dashboard/dash_main.html', context)

def create_event(request):
    form = EventCreateForm()
    if request.method == 'POST':
        form = EventCreateForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            event.participant.add(request.user)
            form.save_m2m()
            messages.success(request, "Event created successfully !")
            return redirect('create_event')
    return render(request, 'event/create_event.html', {'form':form})
            