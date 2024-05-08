from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Course(models.Model):

    PHYSICS = 'Physics'
    CHEMISTRY = 'Chemistry'
    MATHS = 'Maths'
    ENGLISH = 'English'

    SUBJECT_CHOICES = [
        (PHYSICS, 'Physics'),
        (CHEMISTRY, 'Chemistry'),
        (MATHS, 'Maths'),
        (ENGLISH, 'English'),
    ]
    DEFAULT_SUBJECT = PHYSICS

    teacher = models.CharField(max_length=200, unique=True)
    course_subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default=DEFAULT_SUBJECT)

    class Meta:
        ordering = ["-teacher"]

    def __str__(self):
        return f'{self.teacher} - {self.course_subject}'


class Lesson(models.Model):
    
    title = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    video_lesson = CloudinaryField('video', default='placeholder')
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} - {self.course}"


class Comment(models.Model):
    course = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment written by {self.commenter} - {self.body}"