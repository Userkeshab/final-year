from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages, auth

# Create your views here.
def feedback(request):
	if request.method =="POST":		
		feedback = request.POST['feedback']
		Feedback.objects.create(feedback=feedback)


		return redirect('home')
	else:
		return render (request, 'contacts.html')
