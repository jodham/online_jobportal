from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    templatename = 'portal/index.html'
    return render(request, templatename)


def jobs_page(request):
    templatename = 'portal/jobs.html'
    jobs = JobPost.objects.all()
    context = {'Jobs': jobs}
    return render(request, templatename, context)
