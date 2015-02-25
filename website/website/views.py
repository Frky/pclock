from django.shortcuts import render, HttpResponse

from website.clock import Clock

PCLOCK = Clock()

def index(request):
    for job in PCLOCK.sch.get_jobs():
        print job
        print job.trigger
    return HttpResponse(str(PCLOCK) + "<br><br><br>Current delta: " + str(PCLOCK.delta))
