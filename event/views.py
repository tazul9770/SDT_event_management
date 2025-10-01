from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.timezone import now
from django.db.models import Count, Q
from event.models import Event, RSVP
from event.forms import EventCreateForm, RSVPForm
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

    role = request.user.groups.first().name if request.user.groups.exists() else None
    context = {
        'total_events':counts['total_events'],
        'todays_events':counts['todays_events'],
        'upcoming_events':counts['upcoming_events'],
        'past_events':counts['past_events'],
        'events':events,
        'role':role
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

def update_event(request, event_id):
    event = Event.objects.select_related('category').prefetch_related('participant').get(id=event_id)
    form = EventCreateForm(instance=event)
    if request.method == 'POST':
        form = EventCreateForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully !")
            return redirect('update_event', event_id=event.id)
    return render(request, 'event/create_event.html', {'form':form})

def delete_event(request, event_id):
    event = Event.objects.select_related('category').prefetch_related('participant').get(id=event_id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event deleted successfully !")
        return redirect('dashboard')
    return render(request, 'dashboard/dashboard.html')

# def event_detail(request, event_id):
#     role = request.user.groups.first().name if request.user.groups.exists() else None
#     event = Event.objects.select_related('category').prefetch_related('participant').get(id=event_id)
#     return render(request, 'event/event_detail.html', {'event':event, 'role':role})

def rsvp_event(request, event_id):
    event = Event.objects.get(id=event_id)

    role = request.user.groups.first().name if request.user.groups.exists() else None

    # Check if the user already RSVPed
    already_rsvped = RSVP.objects.filter(user=request.user, event=event).exists()

    if request.method == 'POST' and not already_rsvped:
        form = RSVPForm(request.POST)
        if form.is_valid():
            RSVP.objects.create(user=request.user, event=event)
            messages.success(request, "You have successfully RSVPed for this event!")
            return redirect('rsvp_event', event_id=event.id)
    else:
        form = RSVPForm()

    context = {
        'event': event,
        'form': form,
        'already_rsvped': already_rsvped,
        'role': role
    }
    return render(request, 'event/event_detail.html', context)
