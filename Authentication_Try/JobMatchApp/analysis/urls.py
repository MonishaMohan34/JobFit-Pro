from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_1, name='apply_1'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('index/',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('jobroles/',views.jobroles,name='jobroles'),
    path('submit-signup/', views.submit_signup, name='submit_signup'),
    path('submit-login/', views.submit_login, name='submit_login'),
    path('apply/<str:job_title>/', views.apply_now, name='apply_now'),
    path('apply_hello/', views.apply, name='apply'),

]
