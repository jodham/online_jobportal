from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, DetailView, CreateView

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


@login_required
def profile(request):
    if request.method == 'POST':
        userform = UserProfilform(request.POST, instance=request.User)
        userprofile = Userform(request.POST, request.FILES, instance=request.user.userprofile)

        if userform.is_valid() and userprofile.is_valid():
            userform.save()
            userprofile.save()
            return redirect('profile')
    else:
        userform = UserProfilform(instance=request.user)
        userprofile = Userform(instance=request.user.userprofile)

    templatename = 'myapp/profile.html'
    context = {'userprofile': userprofile,
               'userform': userform}

    return render(request, templatename, context)


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            UserProfile.objects.create(user=user, first_name=first_name, second_name=last_name)
            return redirect('login')
    else:
        form = UserRegistration()
    templatename = 'accounts/register.html'
    context = {'form': form}
    return render(request, templatename, context)


# ----------------------------------------------------Createview---------------------->
# ----------------------------------------------------UpdateView---------------------->
class ProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ['first_name', 'second_name', 'gender', 'contact']

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super(ProfileUpdateView, self).form_valid(form)


# ----------------------------------------------------UpdateView---------------------->
# ----------------------------------------------------Createview---------------------->
class ProfileCreateView(CreateView):
    model = UserProfile
    fields = ['first_name', 'second_name', 'gender', 'contact']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EducationCreateView(CreateView):
    model = UserEducatioDetail
    fields = ['cert_degree_name', 'institution_name', 'completion_date', 'starting_date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# --------------------------------x--------------------Createview-----------x----------->

def enter(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        templatename = 'accounts/login.html'
        return render(request, templatename)


def log_out(request):
    logout(request)
    return redirect('login')
