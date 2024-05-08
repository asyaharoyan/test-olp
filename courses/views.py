from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView
from django.contrib import messages
from .models import Course, Lesson, Comment
from .forms import CommentForm

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
    comments = lesson.comments.all().order_by("-created_on")
    comment_count = lesson.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user
            comment.course = lesson
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "courses/course_detail.html",
        {
            "lesson": lesson,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            },
    )
   