from django.urls import path
from event.views import dashboard, create_event, event_detail, update_event, delete_event

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create_event/', create_event, name='create_event'),
    path('detail/<int:event_id>/', event_detail, name='event_detail'),
    path('update_event/<int:event_id>/', update_event, name='update_event'),
    path('delete_event/<int:event_id>/', delete_event, name='delete_event')
]
