from django.contrib import admin
from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from event.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test)
]+ debug_toolbar_urls()
