from django.shortcuts import render
from .models import Contact,Review,Blog
# Create your views here.

def home(request):
	review = {}
	review['comments'] = Review.objects.all()
	return render(request,'index.html',review)


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
		# message['information'] = Information.objects.all()[-1]
		return render(request,'contact.html',message)

	return render(request,'contact.html')

def blog(request):
	blog_view = {}
	blog_view['blogs'] = Blog.objects.all()
	return render(request,'blog-home.html',blog_view)

def blog_detail(request,slugs):
	blog_detail = {}
	blog_detail['blog_details'] = Blog.objects.filter(slug = slugs)
	return render(request,'blog-single.html',blog_detail)
