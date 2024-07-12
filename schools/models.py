from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, related_name='classes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Stream(models.Model):
    name = models.CharField(max_length=255)
    school_class = models.ForeignKey(Class, related_name='streams', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    stream = models.ForeignKey(Stream, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


