from django.contrib import admin
from.models import *
# Register your models here.
admin.site.register(Client)
admin.site.register(Recruiter)



admin.site.register(Job)
admin.site.register(SavedJobs)
admin.site.register(AppliedJobs)