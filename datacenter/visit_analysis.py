def get_duration(visit):
    time_delta = visit.leaved_at - visit.entered_at
    return str(time_delta).split(".")[0]


def is_visit_long(visit, minutes):
    seconds = minutes * 60
    time_delta = visit.leaved_at - visit.entered_at
    return time_delta.total_seconds() > seconds and visit.leaved_at
