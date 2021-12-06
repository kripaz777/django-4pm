from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 200)
	subject = models.TextField()
	message = models.TextField()

	def __str__(self):
		return f"{self.name} {self.email}"


class Review(models.Model):
	name = models.CharField(max_length =200)
	image = models.TextField()
	post = models.CharField(max_length = 200)
	comment = models.TextField()

	def __str__(self):
		return self.name