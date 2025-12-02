from django.db import models

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class Student(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    dob = models.DateField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

class Teacher(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
