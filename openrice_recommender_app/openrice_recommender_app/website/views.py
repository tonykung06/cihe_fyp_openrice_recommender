from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting, Room


def home(request):
    return render(
        request,
        "website/home.html",
        {
            "meetings": Meeting.objects.all(),
        },
    )
