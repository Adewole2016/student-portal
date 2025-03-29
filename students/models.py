from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    matric_no = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=200)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    passport = models.ImageField(upload_to='student_passports/', blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.matric_no})"

class StudentCourseAllocation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.full_name} - {self.course.name}"
