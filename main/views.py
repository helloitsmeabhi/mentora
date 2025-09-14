from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')

 
def dashboard(request):
    return HttpResponse("Dashboard Page")

# Teacher Views
 
def classes(request):
    return HttpResponse("Teacher - My Classes Page")

 
def announcements(request):
    return HttpResponse("Teacher - Announcements Page")

 
def notes(request):
    return HttpResponse("Teacher - Notes Page")

 
def ai_studio(request):
    return HttpResponse("Teacher - AI Studio Page")

 
def analytics(request):
    return HttpResponse("Teacher - Analytics Page")


# Student Views
 
def my_classes(request):
    return HttpResponse("Student - My Classes Page")

 
def assignments(request):
    return HttpResponse("Student - Assignments Page")

 
def study_materials(request):
    return HttpResponse("Student - Study Materials Page")


# Common Views
 
def ai_assistant(request):
    return HttpResponse("AI Assistant Page")

 
def voice_assistant(request):
    return HttpResponse("Voice Assistant Page")

 
def help_view(request):
    return HttpResponse("Help & Support Page")

 
def feedback(request):
    return HttpResponse("Feedback Page")

def register(request):
    return HttpResponse("Register Page")