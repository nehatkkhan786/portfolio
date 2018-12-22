from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField()
	post_image = models.ImageField(upload_to = 'images/')
	post_body = models.TextField()

	def __str__(self):
		return f'{self.title}'

	def summary(self):
		return self.post_body[:100]

	def pretty_pub_date(self):
		return self.pub_date.strftime('%b, %e, %Y')

