from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	id = models.BigAutoField(primary_key=True)
	password = models.CharField(max_length = 150)
	last_login = models.DateTimeField()
	is_superuser = models.IntegerField()
	username = models.CharField(max_length = 150, unique=True)
	first_name  = models.CharField(max_length = 150)
	last_name = models.CharField(max_length = 150)
	email = models.CharField(max_length = 254)
	is_staff = models.IntegerField()
	is_active = models.IntegerField()
	date_joined = models.DateTimeField()
	USERNAME_FIELD = 'username'

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	no = models.IntegerField()
	title = models.CharField(max_length = 150)
	message = models.TextField()
	image = models.ImageField(blank=True, null=True)
	date = models.DateField()
	writer = models.CharField(max_length = 150)

class Subpost(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	post = models.OneToOneField(Post, on_delete=models.CASCADE,null=True)
	comentno = models.IntegerField()
	coment = models.TextField()
	comentdate = models.DateField()
	comentwriter = models.CharField(max_length = 150,null=True)
	
def __str__(self):
	return self.username