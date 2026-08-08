from django.shortcuts import render
from user.forms import ContactForm

def home(request):
    form = ContactForm()
    return render(request, 'home.html', {'form':form})
