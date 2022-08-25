from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    index,
    jobs_page,
    register, enter, log_out, profile,
    JobPostCreate, JobListView
)

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('accounts/login/', enter, name='login'),
    path('accounts/logout/', log_out, name='logout'),
    path('profile/', profile, name='profile'),
    path('jobs/', JobListView.as_view(), name='jobs'),
    path('jobs/new/', JobPostCreate.as_view(), name='newjob'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
