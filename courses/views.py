from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView
from .models import Course, Lesson

# Create your views here.

class LessonList(ListView):
    queryset = Lesson.objects.filter(status=1)
    template_name = 'courses/online_courses.html'
    context_object_name = 'lessons'
    paginate_by = 6


def course_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Lesson.objects.filter(status=1)
    lesson = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "courses/course_detail.html",
        {"lesson": lesson},
    )
   