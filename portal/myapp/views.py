from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import time
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, CreateView, ListView

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


# ----------------------------------------------------ListView---------------------->
@login_required(login_url='/accounts/login')
class UserProfileListView(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = 'myapp/profile.html'
    context_object_name = 'profile'


# ----------------------------------------------------ListView---------------------->
# ----------------------------------------------------UpdateView---------------------->
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['first_name', 'second_name', 'gender', 'contact']

    def form_valid(self, form):
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
# -----------------------------------------------------DetailView----------------------->
class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'myapp/userprofile_detail.html'


# --------------------------------x--------------------DetailView-----------x----------->
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
