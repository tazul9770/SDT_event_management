from django.contrib import admin
from event.models import Event, Category

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'date', 'location')
    search_fields = ('name', 'location')
    list_filter = ('category', 'date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'description')
    search_fields=('name',)
