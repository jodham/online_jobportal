import uuid
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, null=True)
    second_name = models.CharField(max_length=25, null=True)
    contact = models.CharField(max_length=15, null=True)
    user_image = models.ImageField(default='', null=True)
    gender = models.CharField(max_length=6, null=True)

    def __str__(self):
        return f'{self.first_name}userprofile'

    def get_absolute_url(self):
        return reverse('profile-details', kwargs={'pk': self.pk})


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_description = models.TextField()
    company_website_url = models.CharField(max_length=500)
    company_image = models.ImageField()

    def __str__(self):
        return self.user


class UserEducatioDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cert_degree_name = models.CharField(max_length=100)
    institution_name = models.CharField(max_length=100)
    completion_date = models.DateField()
    starting_date = models.DateField()

    def __str__(self):
        return f'{self.cert_degree_name}usereducation'

    def get_absolute_url(self):
        return reverse('education-details', kwargs={'pk': self.pk})


class Skill(models.Model):
    SkillName = models.CharField(max_length=50)

    def __str__(self):
        return self.SkillName


class UserSkillSet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skillNameId = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_set_level = models.CharField(max_length=12)


class JobType(models.Model):
    job_type = models.CharField(max_length=25)

    def __str__(self):
        return self.job_type


class JobLocation(models.Model):
    street_address = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=25)

    def __str__(self):
        return '{}{}'.format(self.city, self.country)


class JobPost(models.Model):
    job_posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    job_post_title = models.CharField(max_length=30, null=True)
    job_type_id = models.ForeignKey(JobType, on_delete=models.CASCADE)
    job_description = models.TextField()
    job_location_id = models.ForeignKey(JobLocation, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(timezone.now)

    def __str__(self):
        return self.job_post_title
