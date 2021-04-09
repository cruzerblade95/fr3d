from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

class Classroom(models.Model):
    name = models.CharField(max_length=130)
    level = models.CharField(max_length=130)

class Course(models.Model):
    name = models.CharField(max_length=130)
    course_id = models.CharField(max_length=130)

class Student(models.Model):
    name = models.CharField(max_length=130)
    student_id = models.CharField(max_length=130)
    course_id = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        verbose_name="course related",
    )

class Lecturer(models.Model):
    name = models.CharField(max_length=130)
    lecturer_id = models.CharField(max_length=130)

class Attendance(models.Model):
    date = models.CharField(max_length=130)
    time = models.CharField(max_length=130)
    student_id = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="student related",
    )


class Subject(models.Model):
    name = models.CharField(max_length=130)
    subject_id = models.CharField(max_length=130)
    classroom_id = models.OneToOneField(
        Classroom,
        on_delete=models.CASCADE,
        verbose_name="classroom related",
    )
    lecturer_id = models.OneToOneField(
        Lecturer,
        on_delete=models.CASCADE,
        verbose_name="classroom related",
    )
