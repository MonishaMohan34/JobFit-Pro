# from django.shortcuts import render

# # Create your views here.
# import os
# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from .models import UploadedFiles
# from django.conf import settings
# from PyPDF2 import PdfReader
# import ollama
# import concurrent.futures
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import User
# from django.contrib.auth.hashers import make_password, check_password


# def load_text_from_pdf(pdf_file):
#     pdf_reader = PdfReader(pdf_file)
#     text = ""
#     for page in pdf_reader.pages:
#         text += page.extract_text()
#     return text

# def analyze_resume_job_description(resume_text, job_description_text):
#     response = ollama.chat(model="llama3.1", messages=[
#         {'role': 'user', 'content': f"Analyze the following resume and job description to determine if the candidate is suitable for the job and give me percentage of suitability.Mention percentage of suitability to job role Resume: {resume_text} Job Description: {job_description_text}"}
#     ])
#     return response['message']['content']

# # def upload_resume(request):
# #     if request.method == 'POST':
# #         # Get uploaded resume file and job description from the form
# #         resume_file = request.FILES['resume']
# #         job_description_text = request.POST['job_description']

# #         # Extract text from the PDF
# #         resume_text = load_text_from_pdf(resume_file)

# #         # Analyze the resume against the job description
# #         analysis_result = analyze_resume_job_description(resume_text, job_description_text)

# #         # Save the result to a text file
# #         output_file_path = os.path.join(settings.MEDIA_ROOT, 'output.txt')
# #         with open(output_file_path, 'w') as file:
# #             file.write(analysis_result)

# #         return JsonResponse({'result': analysis_result, 'file_url': f'/media/output.txt'})

# #     return render(request, 'analysis/upload.html')

# def upload_resume(request):
#     if request.method == 'POST' and request.is_ajax():
#         # Get uploaded resume file and job description from the form
#         resume_file = request.FILES.get('resume')
#         job_description_text = request.POST.get('job_description')

#         if resume_file and job_description_text:
#             # Extract text from the PDF
#             resume_text = load_text_from_pdf(resume_file)

#             # Analyze the resume against the job description
#             analysis_result = analyze_resume_job_description(resume_text, job_description_text)

#             # Save the result to a text file
#             output_file_path = os.path.join(settings.MEDIA_ROOT, 'output.txt')
#             with open(output_file_path, 'w') as file:
#                 file.write(analysis_result)

#             # Return the analysis result and file download URL
#             return JsonResponse({
#                 'result': analysis_result,
#                 'file_url': f'{settings.MEDIA_URL}output.txt'
#             })
#         else:
#             return JsonResponse({'error': 'Missing resume or job description.'}, status=400)

#     return JsonResponse({'error': 'Invalid request.'}, status=400)




# def signup(request):
#     if request.method == 'POST':
#         fullname = request.POST['fullname']
#         email = request.POST['email']
#         password = make_password(request.POST['password'])

#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists.")
#             return redirect('signup')
        
#         User.objects.create(fullname=fullname, email=email, password=password)
#         messages.success(request, "Account created successfully!")
#         return redirect('login')
    
#     return render(request, 'analysis/signup.html')

# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         try:
#             user = User.objects.get(email=email)
#             if check_password(password, user.password):
#                 messages.success(request, "Logged in successfully!")
#                 return redirect('home')
#             else:
#                 messages.error(request, "Incorrect password.")
#         except User.DoesNotExist:
#             messages.error(request, "Email not registered.")
        
#         return redirect('login')

#     return render(request, 'analysis/login.html')
# # views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import messages
# from .models import User



# # def submit_signup(request):
# #     if request.method == 'POST':
# #         fullname = request.POST['fullname']
# #         email = request.POST['email']
# #         password = request.POST['password']
# #         confirm_password = request.POST['confirm-password']

# #         if password == confirm_password:
# #             if User.objects.filter(username=email).exists():
# #                 messages.error(request, "Email is already taken.")
# #                 return redirect('signup')
# #             else:
# #                 user = User.objects.create_user(
# #                     username=email,  
# #                     password=password,
# #                     first_name=fullname  
# #                 )
# #                 user.save()
# #                 messages.success(request, "Account created successfully!")
# #                 return redirect('login')
# #         else:
# #             messages.error(request, "Passwords do not match.")
# #             return redirect('signup')
# #     else:
# #         return redirect('signup')
# def submit_signup(request):
#     if request.method == 'POST':
#         fullname = request.POST['fullname']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm-password']

#         if password == confirm_password:
#             # Check if an account with this email already exists
#             if User.objects.filter(email=email).exists():
#                 messages.error(request, "Email is already taken.")
#                 return redirect('signup')
#             else:
#                 # Create a new user with the provided details
#                 user = User(
#                     email=email,
#                     password=make_password(password),
#                     fullname=fullname
#                 )
#                 user.save()
#                 messages.success(request, "Account created successfully!")
#                 return redirect('login')
#         else:
#             messages.error(request, "Passwords do not match.")
#             return redirect('signup')
#     else:
#         return redirect('signup')
    
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from .models import User  

# def submit_login(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
        
#         user = authenticate(request, username=email, password=password)
        
#         if user is not None:
            
#             login(request, user)
#             messages.success(request, "Logged in successfully!")
#             return redirect('index')  
#         else:
            
#             messages.error(request, "Invalid email or password. Please try again.")
#             return redirect('login')  
#     return render(request, 'login')  



# def jobroles(request):
#     return render(request, 'analysis/jobroles.html')


# # analysis/models.py


# import os
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from django.contrib import messages
# from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth import authenticate, login
# from .models import UploadedFiles, User
# from django.conf import settings
# from PyPDF2 import PdfReader
# import ollama

# # Utility function to extract text from a PDF
# def load_text_from_pdf(pdf_file):
#     pdf_reader = PdfReader(pdf_file)
#     text = ""
#     for page in pdf_reader.pages:
#         text += page.extract_text()
#     return text

# # Function to analyze the resume against the job description using Llama
# def analyze_resume_job_description(resume_text, job_description_text):
#     response = ollama.chat(
#         model="llama3.1",
#         messages=[
#             {
#                 'role': 'user',
#                 'content': (
#                     f"Analyze the following resume and job description to determine "
#                     f"if the candidate is suitable for the job and give a percentage of suitability. "
#                     f"Resume: {resume_text} Job Description: {job_description_text}"
#                 )
#             }
#         ]
#     )
#     return response['message']['content']

# # Upload resume and analyze it
# def upload_resume(request):
#     if request.method == 'POST' and request.is_ajax():
#         resume_file = request.FILES.get('resume')
#         job_description_text = request.POST.get('job_description')

#         if resume_file and job_description_text:
#             # Extract resume text
#             resume_text = load_text_from_pdf(resume_file)

#             # Analyze using Llama
#             analysis_result = analyze_resume_job_description(resume_text, job_description_text)

#             # Save the analysis result in a file
#             output_file_path = os.path.join(settings.MEDIA_ROOT, 'output.txt')
#             with open(output_file_path, 'w') as file:
#                 file.write(analysis_result)

#             # Return the result and file URL
#             return JsonResponse({
#                 'result': analysis_result,
#                 'file_url': f'{settings.MEDIA_URL}output.txt'
#             })

#         return JsonResponse({'error': 'Missing resume or job description.'}, status=400)

#     return JsonResponse({'error': 'Invalid request.'}, status=400)

# # Views for basic pages
# def about(request):
#     return render(request, 'analysis/about.html')

# def contact(request):
#     return render(request, 'analysis/contact.html')

# def index(request):
#     return render(request, 'analysis/index.html')

# def jobroles(request):
#     return render(request, 'analysis/jobroles.html')

# # User signup
# def signup(request):
#     if request.method == 'POST':
#         fullname = request.POST['fullname']
#         email = request.POST['email']
#         password = make_password(request.POST['password'])

#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists.")
#             return redirect('signup')

#         User.objects.create(fullname=fullname, email=email, password=password)
#         messages.success(request, "Account created successfully!")
#         return redirect('login')

#     return render(request, 'analysis/signup.html')

# # User login
# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         try:
#             user = User.objects.get(email=email)
#             if check_password(password, user.password):
#                 login(request, user)  # Log in the user
#                 messages.success(request, "Logged in successfully!")
#                 return redirect('index')
#             else:
#                 messages.error(request, "Incorrect password.")
#         except User.DoesNotExist:
#             messages.error(request, "Email not registered.")

#         return redirect('login')

#     return render(request, 'analysis/login.html')

# # User signup (alternative with password confirmation)
# def submit_signup(request):
#     if request.method == 'POST':
#         fullname = request.POST['fullname']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm-password']

#         if password == confirm_password:
#             if User.objects.filter(email=email).exists():
#                 messages.error(request, "Email is already taken.")
#                 return redirect('signup')
#             else:
#                 User.objects.create(
#                     fullname=fullname,
#                     email=email,
#                     password=make_password(password)
#                 )
#                 messages.success(request, "Account created successfully!")
#                 return redirect('login')
#         else:
#             messages.error(request, "Passwords do not match.")
#             return redirect('signup')

#     return redirect('signup')

# # User login with Django's authentication system
# def submit_login(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = authenticate(request, username=email, password=password)
#         if user:
#             login(request, user)
#             messages.success(request, "Logged in successfully!")
#             return redirect('index')
#         else:
#             messages.error(request, "Invalid email or password. Please try again.")
#             return redirect('login')

#     return render(request, 'analysis/login.html')



import os
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login
from .models import UploadedFiles, User, JobDescription  # Added JobDescription
from django.conf import settings
from PyPDF2 import PdfReader
import ollama

# Utility function to extract text from a PDF
def load_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to analyze the resume against the job description using Llama
def analyze_resume_job_description(resume_text, job_description_text):
    response = ollama.chat(
        model="llama3.1",
        messages=[
            {
                'role': 'user',
                'content': (
                    f"Analyze the following resume and job description to determine "
                    f"if the candidate is suitable for the job and give a percentage of suitability. "
                    f"Resume: {resume_text} Job Description: {job_description_text}"
                )
            }
        ]
    )
    return response['message']['content']

# View for the "Apply Now" button
from django.shortcuts import get_object_or_404

def apply_now(request, job_title):
    job = get_object_or_404(JobDescription, title=job_title)  # Fetch job by title
    if request.method == 'GET':
        return render(request, 'analysis/apply_now.html', {'job': job})


# # Upload resume and analyze it
# def upload_resume(request):
#     if request.method == 'POST':
#         resume_file = request.FILES.get('resume')
#         job_id = request.POST.get('job_id')

#         if resume_file and job_id:
#             # Fetch the job description from the database
#             job = get_object_or_404(JobDescription, id=job_id)
#             job_description_text = job.description

#             # Extract resume text
#             resume_text = load_text_from_pdf(resume_file)

#             # Analyze using Llama
#             analysis_result = analyze_resume_job_description(resume_text, job_description_text)

#             # Save the analysis result in a file
#             output_file_path = os.path.join(settings.MEDIA_ROOT, 'output.txt')
#             with open(output_file_path, 'w') as file:
#                 file.write(analysis_result)

#             # Return the result and file URL
#             return JsonResponse({
#                 'result': analysis_result,
#                 'file_url': f'{settings.MEDIA_URL}output.txt'
#             })

#         return JsonResponse({'error': 'Missing resume or job ID.'}, status=400)

#     return JsonResponse({'error': 'Invalid request.'}, status=400)

# def upload_resume(request):
#     if request.method == 'POST':
#         resume_file = request.FILES.get('resume')
#         job_title = request.POST.get('job_title')

#         try:
#             job = JobDescription.objects.get(title=job_title)  # Fetch job by title
#             job_description_text = job.description

#             # Extract resume text
#             resume_text = load_text_from_pdf(resume_file)

#             # Analyze using Llama
#             analysis_result = analyze_resume_job_description(resume_text, job_description_text)

#             # Save the analysis result in a file
#             output_file_path = os.path.join(settings.MEDIA_ROOT, 'output.txt')
#             with open(output_file_path, 'w') as file:
#                 file.write(analysis_result)

#             # Return the result and file URL
#             return JsonResponse({
#                 'result': analysis_result,
#                 'file_url': f'{settings.MEDIA_URL}output.txt'
#             })

#         except JobDescription.DoesNotExist:
#             return JsonResponse({'error': 'Job description not found.'}, status=400)

#     return JsonResponse({'error': 'Invalid request.'}, status=400)


# def upload_resume(request):
#     if request.method == 'POST':
#         # Get the uploaded resume file
#         resume_file = request.FILES.get('resume')
#         job_title = request.POST.get('job_title')

#         # Validate input
#         if not resume_file:
#             return JsonResponse({'error': 'No resume file uploaded.'}, status=400)
#         if not job_title:
#             return JsonResponse({'error': 'Job title not provided.'}, status=400)

#         try:
#             # Fetch the job description
#             job = JobDescription.objects.get(title=job_title)
#             job_description_text = job.description

#             # Extract resume text
#             resume_text = load_text_from_pdf(resume_file)

#             # Analyze using Llama
#             analysis_result = analyze_resume_job_description(resume_text, job_description_text)

#             # Save the analysis result to a unique file
#             output_file_name = 'output.txt'
#             output_file_path = os.path.join(settings.MEDIA_ROOT, output_file_name)
#             with open(output_file_path, 'w') as file:
#                 file.write(analysis_result)

#             # Return the result and file URL
#             return JsonResponse({
#                 'success': True,
#                 'result': analysis_result,
#                 'file_url': f'{settings.MEDIA_URL}{output_file_name}'
#             })

#         except JobDescription.DoesNotExist:
#             return JsonResponse({'error': 'Job description not found.'}, status=400)

#         except Exception as e:
#             return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)

#     return JsonResponse({'error': 'Invalid request method.'}, status=400)
from django.core.files.storage import FileSystemStorage
import os
def apply_1(request):
    if request.method == 'POST':
        # Get uploaded resume file and job description from the form
        try:
            resume_file = request.FILES['resume']
            upload_dir = 'uploads/resumes/'
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)  # Create the directory if it doesn't exist

            # Use FileSystemStorage to save the file
            fs = FileSystemStorage(location=upload_dir)
            file_name = fs.save(resume_file.name, resume_file)
            file_path = fs.path(file_name)


            return JsonResponse({'message': f'Resume "{resume_file.name}" uploaded successfully!'})
        except Exception as e:
            # Return an error JSON response
            return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
    return render(request, 'analysis/apply.html')


def apply(request):
    if request.method == 'POST':
        # Get uploaded resume file and job description from the form
        resume_file = request.FILES['resume']
        job_description_text = request.POST['job_description']

        # Extract text from the PDF
        resume_text = load_text_from_pdf(resume_file)

        # Analyze the resume against the job description
        analysis_result = analyze_resume_job_description(resume_text, job_description_text)

        # Save the result to a text file
        output_file_path = os.path.join(settings.MEDIA_ROOT, 'output.txt')
        with open(output_file_path, 'w') as file:
            file.write(analysis_result)

        return JsonResponse({'result': analysis_result, 'file_url': f'/media/output.txt'})

    return render(request, 'analysis/apply_admin.html')
# Views for basic pages
def about(request):
    return render(request, 'analysis/about.html')

def contact(request):
    return render(request, 'analysis/contact.html')

def index(request):
    return render(request, 'analysis/index.html')

def jobroles(request):
    jobs = JobDescription.objects.all()  # Fetch all jobs
    return render(request, 'analysis/jobroles.html', {'jobs': jobs})

# User signup
def signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = make_password(request.POST['password'])

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')

        User.objects.create(fullname=fullname, email=email, password=password)
        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'analysis/signup.html')

# User login
# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         try:
#             user = User.objects.get(email=email)
#             if check_password(password, user.password):
#                 login(request, user)  # Log in the user
#                 messages.success(request, "Logged in successfully!")
#                 return redirect('index')
#             else:
#                 messages.error(request, "Incorrect password.")
#         except User.DoesNotExist:
#             messages.error(request, "Email not registered.")

#         return redirect('login')

#     return render(request, 'analysis/login.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Check if the user exists with the given email
            user = User.objects.get(email=email)
            # Validate the password using check_password
            if check_password(password, user.password):
                # Store user details in session for custom authentication
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                messages.success(request, "Logged in successfully!")
                return redirect('index')
            else:
                messages.error(request, "Incorrect password. Please try again.")
        except User.DoesNotExist:
            messages.error(request, "Email not registered. Please sign up first.")

        return redirect('login')

    return render(request, 'analysis/login.html')

# User signup (alternative with password confirmation)
def submit_signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already taken.")
                return redirect('signup')
            else:
                User.objects.create(
                    fullname=fullname,
                    email=email,
                    password=make_password(password)
                )
                messages.success(request, "Account created successfully!")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

    return redirect('signup')

# User login with Django's authentication system
# def submit_login(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = authenticate(request, username=email, password=password)
#         if user:
#             login(request, user)
#             messages.success(request, "Logged in successfully!")
#             return redirect('index')
#         else:
#             messages.error(request, "Invalid email or password. Please try again.")
#             return redirect('login')

#     return render(request, 'analysis/login.html')


from analysis.models import User  # Import your custom User model

def submit_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Check if the user exists with the given email and password
            user = User.objects.get(email=email, password=password)
            # Store user details in the session to mark the user as logged in
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            messages.success(request, "Logged in successfully!")
            return redirect('index')
        except User.DoesNotExist:
            messages.success(request, "Logged in successfully")
            return redirect('login')

    return render(request, 'analysis/login.html')