from django.contrib.auth.models import Group

def role(request):
    if request.user.is_authenticated:
        role = request.user.groups.first().name if request.user.groups.exists() else None
        return {'role': role}
    return {'role': None}
