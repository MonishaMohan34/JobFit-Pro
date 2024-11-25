from django.db import models



class UploadedFiles(models.Model):
    resume = models.FileField(upload_to='resumes/')
    job_description = models.FileField(upload_to='job_descriptions/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



class User(models.Model):
    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)

    def __str__(self):
        return self.email




class JobDescription(models.Model):
    title = models.CharField(max_length=200)  # Job role/title
    description = models.TextField()  # Detailed job description
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for record creation

    def __str__(self):
        return self.title

