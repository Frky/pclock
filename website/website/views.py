from django.shortcuts import render, HttpResponse

from website.clock import Clock

PCLOCK = Clock()

def index(request):
    for job in PCLOCK.sch.get_jobs():
        print job
        print job.trigger
    context = dict()
    context["pclock"] = PCLOCK.pclock()
    context["oclock"] = PCLOCK.oclock()
    context["delta"] = str(PCLOCK.delta)

    context["second"] = PCLOCK.pclock().second
    context["minute"] = PCLOCK.pclock().minute
    context["hour"] = PCLOCK.pclock().hour

    context["hour_lap"] = PCLOCK.laps["hour"]
    context["minute_lap"] = PCLOCK.laps["minute"]
    context["second_lap"] = PCLOCK.laps["second"]

    return render(request, "website/index.html", context)
