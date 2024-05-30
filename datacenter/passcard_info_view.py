from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404

import datacenter.visit_analysis as visit_analysis


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode__contains=passcode)
    this_passcard_visits = []
    for visit in Visit.objects.filter(
            passcard=passcard):
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': visit_analysis.get_duration(visit),
                'is_strange': visit_analysis.is_visit_long(visit, 60),
            })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
