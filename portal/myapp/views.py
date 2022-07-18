from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, DetailView

from .forms import *
from .models import *


# Create your views here.
def index(request):
    templatename = 'myapp/index.html'
    return render(request, templatename)


def jobs_page(request):
    templatename = 'myapp/jobs.html'
    jobs = JobPost.objects.all()
    jobcount = JobPost.objects.all().count()
    context = {'jobs': jobs, 'jobcount': jobcount}
    return render(request, templatename, context)


def profile(request):
    if request.method == 'POST':
        userform = UserProfilform(request.POST, instance=request.User)
        userprofile = Userform(request.POST, request.FILes, instance=request.user.userprofile)

        if userform.is_valid() and userprofile.is_valid():
            userform.save()
            userprofile.save()
            return redirect('profile')
    else:
        userform = UserProfilform(instance=request.user)
        userprofile = Userform(instance=request.user.userprofile)

    templatename = 'myapp/userprofile_detail.html'
    context = {'userprofile': userprofile,
               'userform': userform}

    return render(request, templatename, context)
