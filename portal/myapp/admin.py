from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(CompanyProfile)
admin.site.register(UserEducatioDetail)
admin.site.register(SkillLevel)
admin.site.register(skillExperience)
admin.site.register(Skill)
admin.site.register(JobPost)
admin.site.register(JobType)
admin.site.register(JobLocation)
