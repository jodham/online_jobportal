from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    templatename = 'portal/index.html'
    return render(request, templatename)


def jobs_page(request):
    templatename = 'portal/jobs.html'
    jobs = JobPost.objects.all()
    jobcount = JobPost.objects.all().count()
    context = {'jobs': jobs, 'jobcount': jobcount}
    return render(request, templatename, context)

def profile_page(request):
    templatename = 'portal/profile.html'
    user = request.user
    context = {'user': user}
    return render(request, templatename, context)