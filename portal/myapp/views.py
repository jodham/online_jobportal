from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, CreateView, ListView, DeleteView

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
            UserEducatioDetail.objects.create(user=user)
            return redirect('login')
    else:
        form = UserRegistration()
    templatename = 'accounts/register.html'
    context = {'form': form}
    return render(request, templatename, context)


# ----------------------------------------------------ListView---------------------->
def profile(request):
    educationlist = UserEducatioDetail.objects.all()

    if request.method == 'POST':
        form = userprofileform(data=request.POST, instance=request.user)
        userextradata = Userdetailsform(request.POST, request.FILES, instance=request.user.userprofile)
        usereducationcreate = UserEducationCreate(request.POST)
        if form.is_valid() and userextradata.is_valid() and usereducationcreate.is_valid():
            form.save()
            userextradata.save()
            usereducationcreate.save()
            return redirect('profile')
        else:
            templatename = 'myapp/profile.html'
            userextradata = Userdetailsform(instance=request.user.userprofile)
            form = userprofileform(instance=request.user)
            usereducationcreate = UserEducationCreate(request.POST)
            error = messages.warning(request, "correct error below!!")
            context = {'error': error, 'form': form, 'userextradata': userextradata,
                       'usereducationcreate': usereducationcreate}
            return render(request, templatename, context)
    else:
        form = userprofileform(instance=request.user)
        usereducationcreate = UserEducationCreate()
        userextradata = Userdetailsform(instance=request.user.userprofile)

        templatename = 'myapp/profile.html'
        context = {'form': form, 'userextradata': userextradata, 'usereducationcreate': usereducationcreate,
                   "educationlist": educationlist}
        return render(request, templatename, context)


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


# ----------------------------------------------------ListView------------------------>
class JobListView(ListView):
    model = JobPost
    template_name = 'myapp/jobs.html'
    context_object_name = 'jobs'
    ordering = ['-date_posted']


class SkillListView(ListView):
    model = Skill
    context_object_name = 'skill'
    ordering = ['-dateposted']


# -----------------------x-----------------------------ListView------------x---------->
# ----------------------------------------------------UpdateView---------------------->
class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    fields = ['field', 'level', 'experience', 'SkillName', 'fieldImage']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(SkillUpdateView, self).form_valid(form)


# ----------------------------------------------------UpdateView---------------------->
# ----------------------------------------------------Createview---------------------->
class JobPostCreate(CreateView):
    model = JobPost
    fields = ['job_post_title', 'job_type_id', 'job_description', 'job_location_id']

    def form_valid(self, form):
        form.instance.job_posted_by = self.request.user
        return super(JobPostCreate, self).form_valid(form)

    def test_func(self):
        mypost = self.get_object()
        if self.request.user == mypost.user:
            return True
        return False


class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    fields = ['field', 'level', 'experience', 'SkillName', 'fieldImage']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(SkillCreateView, self).form_valid(form)


# --------------------------------x--------------------Createview-----------x----------->
# -----------------------------------------------------DetailView----------------------->
class SkillDetailView(LoginRequiredMixin, DetailView):
    model = Skill


class JobDetailView(LoginRequiredMixin, DetailView):
    model = JobPost


# --------------------------------x--------------------DetailView-----------x----------->

# --------------------------------x--------------------DeletelView-----------x----------->

class SkillDeleteView(LoginRequiredMixin, DeleteView):
    model = Skill
    success_url = reverse_lazy('myskill')

# --------------------------------x--------------------DeleteView-----------x----------->
