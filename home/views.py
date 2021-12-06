from django.shortcuts import render
from .models import Contact
# Create your views here.

def home(request):

	return render(request,'index.html')


def about(request):

	return render(request,'about.html')


def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		data = Contact.objects.create(
			name = name,
			email = email,
			subject = subject,
			message = message
			)
		data.save()
		message = {'success':'The form is submitted'}
		return render(request,'contact.html',message)

	return render(request,'contact.html')