from . import views
from django.urls import path

urlpatterns = [
    path('', views.LessonList.as_view(), name='courses'),
    path('<slug:slug>/', views.course_detail, name='course_detail'),
]