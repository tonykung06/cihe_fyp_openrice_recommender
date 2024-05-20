from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from meetings.forms import MeetingForm, RoomForm
from meetings.models import Meeting, Room


def home(request):
    return render(
        request,
        "meetings/home.html",
        {
            "message": "Please manage the rooms and meetings below.",
            "meetings": Meeting.objects.all(),
        },
    )


def detail(request, id: int):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def room_detail(request, id: int):
    room = get_object_or_404(Room, pk=id)
    return render(request, "meetings/room_detail.html", {"room": room})


def room_list(request):
    return render(
        request,
        "meetings/room_list.html",
        {
            "rooms": Room.objects.all(),
        },
    )


def new(request):
    form = MeetingForm()
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "meetings/new.html", {"form": form})


def new_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "meetings/new.html", {"form": form})
