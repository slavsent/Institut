from django.db import models
from uuid import uuid4


class Student(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    firstname = models.CharField(max_length=256, verbose_name="firstname")
    surname = models.CharField(max_length=256, verbose_name="surname")
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.firstname}"

    def delete(self, *args):
        self.deleted = True
        self.save()


class CardStudent(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    id_student = models.CharField(max_length=256, verbose_name="id_student")
    name = models.CharField(max_length=256, verbose_name="name")
    deleted = models.BooleanField(default=False)

    def delete(self, *args):
        self.deleted = True
        self.save()


class Courses(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=256, verbose_name="Name")
    number = models.IntegerField(verbose_name="Number")
    student = models.ManyToManyField(Student)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"

    def delete(self, *args):
        self.deleted = True
        self.save()


class Teachers(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    firstname = models.CharField(max_length=256, verbose_name="firstname")
    surname = models.CharField(max_length=256, verbose_name="surname")
    title = models.CharField(max_length=256, verbose_name="title")
    deleted = models.BooleanField(default=False)

    def delete(self, *args):
        self.deleted = True
        self.save()


class Terms(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    number = models.IntegerField(verbose_name="Number")
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    def delete(self, *args):
        self.deleted = True
        self.save()


class TermCourses(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    term = models.ForeignKey(Terms, on_delete=models.CASCADE)
    date_begin = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def delete(self, *args):
        self.deleted = True
        self.save()
