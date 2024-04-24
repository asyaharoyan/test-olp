from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import Course, Lesson

# Create your views here.

class LessonList(ListView):
    queryset = Lesson.objects.filter(status=1)
    template_name = 'courses/online_courses.html'
    context_object_name = 'lessons'
    paginate_by = 6