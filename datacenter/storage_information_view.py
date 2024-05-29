from datacenter.models import Visit
from django.shortcuts import render


def get_duration(visit):
    time_delta = visit.leaved_at - visit.entered_at
    return str(time_delta).split(".")[0]


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': get_duration(visit),
            })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
