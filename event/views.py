from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return render(request, 'test.html', {"message":"This my first context"})