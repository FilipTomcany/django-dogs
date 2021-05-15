from django.http.response import Http404, HttpResponseServerError
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Race

def home(request, *arcs, **kwargs):
    return HttpResponse("Hello")

def home_details_view(request, pk, *arcs, **kwargs):
    try:
        obj = Race.objects.get(pk=pk)
    except Race.DoesNotExist:
        raise Http404
    return HttpResponse(f"číslo plemena {obj.pk}")
    
