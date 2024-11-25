
from django.test import TestCase

# Test case 1

from .models import UploadedFiles
from django.core.files.uploadedfile import SimpleUploadedFile

class UploadedFilesModelTest(TestCase):
    def test_uploaded_files_model(self):
        
        resume_file = SimpleUploadedFile("resume2.pdf", b"Resume content")
        job_description_file = SimpleUploadedFile("job_description.pdf", b"Job Description content")

        
        uploaded_file = UploadedFiles.objects.create(
            resume=resume_file,
            job_description=job_description_file
        )

        # Assert that the uploaded resume file name starts with "resumes/resume2"
        self.assertTrue(uploaded_file.resume.name.startswith("resumes/resume2"))



# Test Case 2

# analysis/tests.py

from .views import analyze_resume_job_description

class ResumeAnalysisFunctionTest(TestCase):
    def test_analyze_resume_job_description(self):
        resume_text = "JavaScript,HTML,CSS,.NET,React.js,Angular.js,Node.js,Rest APIs,Spring,SOAP,Scrum/Agile"
        job_description_text = "Looking for a candidate skilled in Mongodb,Html,CSS,JS,Angular , Node."

        result = analyze_resume_job_description(resume_text, job_description_text)
        
        self.assertIn("percentage", result)  # You may have to adjust this based on actual response content


# Test case 3

# analysis/tests.py

from django.urls import reverse
from django.test import Client, TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class FileUploadViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_file_upload(self):
        
        pdf_path = os.path.join(os.path.dirname(__file__), 'resume2.pdf')
        
        with open(pdf_path, 'rb') as pdf_file:
            resume = SimpleUploadedFile("resume2.pdf", pdf_file.read(), content_type="application/pdf")
        
        job_description = "Looking for a candidate skilled in Mongodb,Html,CSS,JS,Angular , Node."
        
        response = self.client.post(reverse('upload_resume'), {
            'resume': resume,
            'job_description': job_description,
        })
        
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, "result")  