from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Album
from .models import Artist
from .models import Track
from .models import Genre

def index(request):
    

    context = {
        "album": album
    }

    return render(request, "music/index.html", context)
