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

    teacher = models.CharField(max_length=200, unique=True)


class Lesson(models.Model):
    
    title = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    video_lesson = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title