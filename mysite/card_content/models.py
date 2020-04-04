from django.db import models

# Create your models here.


class Profile(models.Model):
	title = models.CharField(max_length=100)
	navbar_brand = models.CharField(max_length=10)
	def __str__(self):
		return self.title