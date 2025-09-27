from django.urls import path
from event.views import dashboard, create_event

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create_event/', create_event, name='create_event')
]
