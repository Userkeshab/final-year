from django.urls import path

from. import views

urlpatterns = [
    path('client_register/', views.client_register, name='client_register'),
    path('recruiter_register/', views.recruiter_register, name='recruiter_register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('landingpage/', views.landingpage, name='landingpage'),
    path('seeker_dashboard/', views.seeker_dashboard, name='seeker_dashboard'),
    path('seeker_profile/', views.seeker_profile, name='seeker_profile'),
    path('recruiter_profile/', views.recruiter_profile, name='recruiter_profile'),

    path('post_job/', views.post_job, name='post_job'),
    








    path('job_home/', views.job_home, name='job_home'),
    path('delete_job/<int:id>', views.delete_job, name='delete_job'),

    path('savedJobs/', views.savedJobs, name='saved_jobs'),
    path('appliedJobs/', views.appliedJobs, name='appliedJobs'),
    path('save_job/<int:job_id>', views.save_job, name='save_job'),
    path('apply_job/<int:job_id>', views.apply_job, name='apply_job'),

    path('remove_job/<int:id>', views.remove_job, name='remove_job'),
    path('applicants/', views.applicants, name='applicants'),
    path('applicants/<int:job_id>', views.applicant, name='applicant'),

    path('job_details/', views.job_details, name='job_details'),

    path('remove_applied_job/<int:id>', views.remove_applied_job, name='remove_applied_job'),

    path("search", views.search, name="search"),
 

]