from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserDetails(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	mobile_number = models.CharField(max_length=10)
	residentail_address = models.CharField(max_length=100)
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=25)
	pincode = models.CharField(max_length=7)
	date_of_birth = models.DateField()
	email = models.EmailField()

class Experience(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	company = models.CharField(max_length=30, blank=True, null=True)
	location = models.CharField(max_length=30, blank=True, null=True)
	job_title = models.CharField(max_length=30, blank=True, null=True)
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)
	job_summary = models.CharField(max_length=150, blank=True, null=True)


class Education(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	school_name = models.CharField(max_length=255)
	location = models.CharField(max_length=255)
	start_date = models.DateField()
	end_date = models.DateField()
	edu_summary = models.CharField(max_length=255)
	board = models.CharField(max_length=30)

class Skills(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	skill = models.CharField(max_length=50)


class Projects(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	project_name = models.CharField(max_length=100)
	project_descpription = models.CharField(max_length=200)


class Hobbies(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	hobby = models.CharField(max_length=50)


class Languages(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	language = models.CharField(max_length=30)
