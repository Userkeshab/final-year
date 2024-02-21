from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages, auth
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse


# Create your views here.
def client_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        username = request.POST['username']
        
        contact = request.POST['contact']
        gender = request.POST['gender']
        address = request.POST['address']
        image = request.FILES['image']
        education = request.POST['education']
        interested_in = request.POST['interested_in']
        
        if password1 != password2:
            messages.info(request, 'passwords are different')
            return redirect('client_register')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'username taken')
            return redirect('client_register')
           
        if User.objects.filter(email=email).exists():
            messages.info(request, 'email taken')
            return redirect('client_register')
        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        Client.objects.create(user=user, contact=contact, gender=gender, address=address,education=education,interested_in=interested_in, image=image)
        auth.login(request, user)
     
        auth.login(request,user)
        return redirect('seeker_dashboard')


    else:
        return render(request,'client_register.html')



    


def recruiter_register(request):
    if request.method == 'POST':
        password = request.POST['password']
        password1 = request.POST['password1']
        username = request.POST['username']

        company_name = request.POST['company_name']
        company_contact = request.POST['company_contact']
        company_location = request.POST['company_location']
        company_email = request.POST['company_email']
        company_type = request.POST['company_type']
        company_details = request.POST['company_details']

        recruiter_name = request.POST['recruiter_name']
        recruiter_contact = request.POST['recruiter_contact']
        if password1 != password1:
            messages.info(request, 'passwords are different')
            return redirect('recruiter_register')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'username taken')
            return redirect('recruiter_register')

        user = User.objects.create_user(username = username, password = password1, is_staff=True)
        Recruiter.objects.create(user = user, company_name=company_name, company_contact=company_contact,
        company_location=company_location, company_email=company_email, company_type=company_type,
        company_details=company_details, recruiter_name=recruiter_name, recruiter_contact=recruiter_contact)
        
        auth.login(request,user)
        return redirect('landingpage')
    else:
        return render(request,'recruiter_register.html')





def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_superuser:
            auth.login(request, user)
            return HttpResponseRedirect('/admin/')

        elif user is not None and user.is_staff:
            auth.login(request, user)
            return redirect('landingpage')

        elif user is not None and not user.is_staff and not user.is_superuser:
            auth.login(request, user)
            return redirect('seeker_dashboard')

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def landingpage(request):
    if request.user.is_authenticated:
        return render(request, 'landingpage.html')
    else:
        messages.info(request,'please login to access this page.')
        return redirect('home')

def seeker_dashboard(request):
    if request.user.is_authenticated:
        jobs = Job.objects.all()
        
        user_details = Client.objects.get(user=request.user) 
        rec_jobs = Job.objects.filter(job_category=user_details.interested_in)
        print(rec_jobs)

        return render(request, 'seeker_dashboard.html', {'jobs': jobs, 'rec_jobs' : rec_jobs})
    else:
        messages.info(request,'please login to access this page.')
        return redirect('home')
    

# profile

def seeker_profile(request):
    if request.user.is_authenticated:
        userdata = Client.objects.filter(user=request.user)
        # for data in userdata:
        #     print(data.contact)
        return render(request, 'seeker_profile.html', {'userdata': userdata })
    else:
        messages.info(request, 'You are not logged in. Please log in to continue')
        return redirect('home')

def recruiter_profile(request):
    if request.user.is_authenticated:
        userdata = Recruiter.objects.filter(user=request.user)
        return render(request, 'recruiter_profile.html', {'userdata': userdata })
    else:
        messages.info(request, 'You are not logged in. Please log in to continue')
        return redirect('home')


# jobs
def post_job(request):
    form = JobForm()    
    user=User.objects.get(username=request.user)
    
    form.fields['user'].initial  = user.id
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.fields['user'] = user
            
            form.save()
        return redirect('job_home')
    return render(request, 'post_job.html', {'form': form})









def job_home(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'job_home.html', {'jobs': jobs})



def job_details(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'job_details.html', {'jobs': jobs})


    
def savedJobs(request):
    jobs=SavedJobs.objects.filter(user=request.user)
    return render(request, 'savedjobs.html',{'jobs':jobs})



def appliedJobs(request):
    jobs=AppliedJobs.objects.filter(user=request.user)
    return render(request, 'appliedjobs.html',{'jobs':jobs})



def applicants(request):
    jobs=Job.objects.filter(user=request.user)
    return render(request, 'applicants.html',{'jobs':jobs})



def applicant(request, job_id):
    jobs=AppliedJobs.objects.filter(job=job_id, job__user=request.user)
    if(jobs):
        job=jobs[0]
    else:
        job='Sorry! Nobody has applied to this job yet.'
    return render(request, 'applicant.html',{'jobs':jobs,'job':job})





def delete_job(request,id):
    obj = Job.objects.get(job_id= id)
    obj.delete()
    messages.info(request, 'job deleted')
    return redirect('job_home')



def remove_job(request,id):
    obj = SavedJobs.objects.get(job_id= id)
    obj.delete()
    messages.info(request, 'job removed')
    return redirect('seeker_dashboard')



def remove_applied_job(request,id):
    obj = AppliedJobs.objects.get(job_id= id)
    obj.delete()
    messages.info(request, 'job removed')
    return redirect('seeker_dashboard')



def save_job(request,job_id):
    if SavedJobs.objects.filter(job_id=job_id, user=request.user).exists():
            messages.info(request, 'you already saved this job')
            return redirect('seeker_dashboard')
    else:
        if request.user.is_authenticated:
            try:
                job=Job.objects.get(job_id=job_id)
                user=User.objects.get(username=request.user)
                saved_Jobs=SavedJobs(job=job,user=user)
                saved_Jobs.save()
                return redirect('saved_jobs')
            except:
                return redirect('saved_jobs')



def apply_job(request,job_id):
    if AppliedJobs.objects.filter(job_id=job_id, user=request.user).exists():
            messages.info(request, 'you already applied for this job')
            return redirect('seeker_dashboard')
    else:
        if request.user.is_authenticated:
            try:
                job=Job.objects.get(job_id=job_id)
                user=User.objects.get(username=request.user)
                applied_jobs=AppliedJobs(job=job,user=user)
                applied_jobs.save()
                return redirect('appliedJobs')
            except:
                return redirect('appliedJobs')     


def search(request):
    
    query = request.GET['query']
    jobs = Job.objects.filter(job_title__icontains=query)
    allJob =  {'jobs': jobs}
    return render(request, 'search.html',allJob)


def CV(request):
    if request.user.is_authenticated:
        user_details = Client.objects.filter(user=request.user)[0]
        userinfo=User.objects.filter(username=request.user)[0]
        if user_details and userinfo:
            print(userinfo.username)
            print(userinfo.email)
            print(userinfo.first_name)
            print(userinfo.last_name)
            print(user_details.image)
            print(user_details.contact)
            print(user_details.education)
            print(user_details.interested_in)
            return render(request, 'cv.html', {'user_details': user_details, 'userinfo': userinfo})

        else:
            return HttpResponse("Please complete your profile to view your CV.")
    else:
        return redirect('/accounts/login/')
