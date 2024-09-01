from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField

from django.db import models

class Profile(models.Model):
    # Fields
    pic = models.ImageField(upload_to="images/")
    full_name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    linkedin_profile = models.URLField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    institution_name = models.CharField(max_length=255)
    graduation_date = models.DateField()

    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255, blank=True, null=True)
    job_year = models.DateField()
    job_desc = models.TextField()

    hobby = models.CharField(max_length=255)
    skill = models.CharField(max_length=255)
    certification = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    language_level = models.CharField(max_length=50, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Fluent', 'Fluent'), ('Native', 'Native')])

    project = models.CharField(max_length=255)
    project_desc = models.TextField()
    project_sdate = models.DateField()
    project_edate = models.DateField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)

    @property
    def __grouped_fields__(self):
        return {
            "Personal Information": ["pic", "full_name", "address", "bio", "contact_number", "email", "linkedin_profile"],
            "Education": ["degree", "field_of_study", "institution_name", "graduation_date"],
            "Work Experience": ["job_title", "company_name", "company_location", "job_year", "job_desc"],
            "Skills and Certifications": ["hobby", "skill", "certification"],
            "Language Proficiency": ["language", "language_level"],
            "Projects": ["project", "project_desc", "project_sdate", "project_edate"],
        }


    def __str__(self):
        return self.user
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name + " - " + str(self.user) + " | " + str(self.email)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + str(self.email) + " | " +  str(self.date) + " : " +str(self.desc)