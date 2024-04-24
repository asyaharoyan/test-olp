from . import views
from django.urls import path

urlpatterns = [
    path('', views.LessonList.as_view(), name="courses"),
]