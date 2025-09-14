from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='index'),
    path("dashboard/", dashboard, name="dashboard"),

    # Teacher URLs
    path("classes/", classes, name="classes"),
    path("announcements/", announcements, name="announcements"),
    path("notes/", notes, name="notes"),
    path("ai-studio/", ai_studio, name="ai_studio"),
    path("analytics/", analytics, name="analytics"),

    # Student URLs
    path("my-classes/", my_classes, name="my_classes"),
    path("assignments/", assignments, name="assignments"),
    path("study-materials/", study_materials, name="study_materials"),

    # Common URLs
    path("ai-assistant/", ai_assistant, name="ai_assistant"),
    path("voice-assistant/", voice_assistant, name="voice_assistant"),
    path("help/", help_view, name="help"),
    path("feedback/", feedback, name="feedback"),
    path("register/", register, name="register"),
]