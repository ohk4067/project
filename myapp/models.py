from django.db import models

# Create your models here.
class User(models.Model):
	id = models.BigAutoField(primary_key=True)
	password = models.CharField(max_length = 30)
	username = models.CharField(max_length = 30)
	age = models.CharField(max_length = 3)
	sex  = models.CharField(max_length = 6)
	email = models.EmailField()

	def __str__(self):
		return self.username