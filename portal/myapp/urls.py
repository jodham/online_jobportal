from django.urls import path
from . views import(
        index,
        jobs_page,
        register, enter, log_out, profile, ProfileListView,
        ProfileCreateView, EducationCreateView, ProfileUpdateView, UserProfileDetailView
)

urlpatterns = [
    path('', index, name='index'),
    path('jobs/', jobs_page, name='jobs'),
    path('profile/', ProfileListView.as_view(), name='profile'),
    path('register/', register, name='register'),
    path('accounts/login/', enter, name='login'),
    path('accounts/logout/', log_out, name='logout'),
    path('userdetails/', ProfileCreateView.as_view(), name='profile-create'),
    path('userprofile/<int:pk>/details', UserProfileDetailView.as_view(), name='profile-details'),
    path('updatedetails/<int:id>/update', ProfileUpdateView.as_view(), name='profile-update'),
    path('education/', EducationCreateView.as_view(), name='education-create'),
]
