from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	id = models.BigAutoField(primary_key=True)
	password = models.CharField(max_length = 150)
	last_login = models.DateTimeField()
	is_superuser = models.BooleanField()
	username = models.CharField(max_length = 150, unique=True)
	first_name  = models.CharField(max_length = 150)
	last_name = models.CharField(max_length = 150)
	email = models.CharField(max_length = 254)
	is_staff = models.BooleanField()
	is_active = models.BooleanField()
	date_joined = models.DateTimeField()
	USERNAME_FIELD = 'username'

class Post(models.Model):
	no = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length = 150)
	message = models.TextField()
	image = models.ImageField(blank=True, null=True)
	date = models.DateField()
	writer = models.CharField(max_length = 150)

class Subpost(models.Model):
	comentno = models.BigAutoField(primary_key=True)
	coment = models.TextField()
	comentdate = models.DateTimeField()
	comentwriter = models.CharField(max_length = 150,null=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
	
def __str__(self):
	return self.username