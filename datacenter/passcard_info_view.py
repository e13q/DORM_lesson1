from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def get_duration(visit):
    time_delta = visit.leaved_at - visit.entered_at
    return str(time_delta).split(".")[0]


def is_visit_long(visit, minutes):
    seconds = minutes * 60
    time_delta = visit.leaved_at - visit.entered_at
    if time_delta.total_seconds() > seconds and visit.leaved_at:
        return True
    else:
        return False


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode__contains=passcode)
    this_passcard_visits = []
    for visit in Visit.objects.filter(
            passcard__owner_name__contains=passcard.owner_name):
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': get_duration(visit),
                'is_strange': is_visit_long(visit, 60),
            })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
