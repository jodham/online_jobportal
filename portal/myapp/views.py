from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

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
        userprofileupdate = UserProfileUpdate(request.POST, instance=request.user)
        userdetailform = UserDetailUpdate(request.POST, request.FILES, instance=request.user.userprofile)

        if userdetailform.is_valid() and userprofileupdate.is_valid():
            userprofileupdate.save()
            userdetailform.save()
            return HttpResponseRedirect('index')
    else:
        userprofileupdate = UserProfileUpdate(request.POST, instance=request.user)
        userdetailform = UserDetailUpdate(request.POST, request.FILES, instance=request.user.userprofile)
        templatename = 'myapp/userprofile_form.html'
        context = {'userprofileupdate': userprofileupdate, 'userdetailform': userdetailform}
        return render(request, templatename, context)
