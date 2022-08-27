from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    index,
    jobs_page,
    register, enter, log_out, profile, SkillUpdateView, SkillDeleteView,
    JobPostCreate, JobListView, SkillListView, SkillDetailView, SkillCreateView, JobDetailView
)

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('accounts/login/', enter, name='login'),
    path('accounts/logout/', log_out, name='logout'),
    path('profile/', profile, name='profile'),
    path('jobs/', JobListView.as_view(), name='jobs'),
    path('jobs/new/', JobPostCreate.as_view(), name='newjob'),
    path('job/<int:pk>/detail', JobDetailView.as_view(), name='job-detail'),

    path('skills/', SkillListView.as_view(), name='myskills'),
    path('skill/<int:pk>/detail/', SkillDetailView.as_view(), name='skill-detail'),
    path('skill/new/', SkillCreateView.as_view(), name='new-skill'),
    path('skill/<int:pk>/update/', SkillUpdateView.as_view(), name='skill-update'),
    path('skill/<int:pk>/delete/', SkillDeleteView.as_view(), name='skill-delete')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
