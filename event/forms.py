from django import forms
from event.models import Event, RSVP

class EventCreateForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=True 
    )
    class Meta:
        model = Event
        fields = ['name', 'description', 'image', 'date', 'location', 'category']

class RSVPForm(forms.Form):
    confirm = forms.BooleanField(
        required=True,
        label="I want to RSVP for this event"
    )