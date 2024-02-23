from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Client(models.Model):    
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True,null=True, upload_to='seeker/', default='user.jpg')
    education = models.CharField(max_length=50, null=True)
    interested_in = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.username

class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=15, null=True)
    company_contact = models.CharField(max_length=30,null=True)
    company_location = models.CharField(max_length=15, null=True)
    company_email = models.CharField(max_length=15, null=True)
    company_type = models.CharField(max_length=15, null=True)
    company_details = models.CharField(max_length= 1000,null = True)

    recruiter_name = models.CharField(max_length=15, null=True)
    recruiter_contact = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.user.username




# job form
class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    job_id = models.AutoField(primary_key=True, null=False)
    JOB_CHOICES = (
        ('finance', 'Finance'),
        ('marketing', 'Marketing'),
        ('webdesign', 'Webdesign'),
        ('accountant', 'Accountant'),
        ('banking', 'Banking'),
        ('security', 'Security'),
        ('teaching', 'Teaching'),
        ('engineering', 'Engineering'),
        ('it', 'IT'),
        ('others', 'Others')
    )
    job_title = models.CharField(max_length=200)
    job_position = models.CharField(max_length=200)
    job_category = models.CharField(max_length=250, choices=JOB_CHOICES, default='others')
    job_description = models.TextField()
    job_phone = models.CharField(max_length=100)
    job_email = models.EmailField()
    job_website = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.job_title


class SavedJobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=True, null=True)


class AppliedJobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=True, null=True)