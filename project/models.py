from django.db import models
from django.urls import reverse

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length= 50)
    description = models.CharField(max_length= 500)
    image = models.ImageField(upload_to='resume/images')
    url = models.URLField(blank=True)
    
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={
            "project_id": self.id
            })


class About(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    descript = models.CharField(max_length=500)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    
    
    def __str__(self):
        return self.fname
    
    
class Experience(models.Model):
    job_designation = models.CharField(max_length = 50)
    company = models.CharField(max_length = 50)
    discription = models.CharField(max_length = 500)
    start_date = models.DateField()
    end_date = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.job_designation
    