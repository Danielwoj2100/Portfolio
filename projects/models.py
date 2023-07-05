from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class Technology(models.Model):
    technologies = models.CharField(max_length=25)

    def __str__(self):
        return self.technologies

class Project(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    image = models.ImageField(upload_to='img/')
    url = models.URLField(max_length=200, blank= True)
    creationDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    school = models.CharField(max_length=40)
    fieldofstudy = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    start = models.DateField()
    prognozedend = models.DateField(null=True, blank=True)
    finished = models.BooleanField(default=False)
    def clean(self):
        if self.finished and self.prognozedend is None:
            raise ValidationError('Prognozedend must be provided when finished is True.')

    def __str__(self):
        return self.school

class Language(models.Model):
    Language_levels = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Fluent', 'Fluent'),
        ('Native', 'Native'),
    )
    name = models.CharField(max_length=20)
    level = models.CharField(max_length=20, choices=Language_levels)
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Link(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField(max_length=100)
    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=20)
    start_date = models.DateField()
    stop_date = models.DateField()
    duration = models.DurationField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.start_date and self.stop_date:
            self.duration = self.stop_date - self.start_date
        super().save(*args, **kwargs)

    def __str__(self):
        return self.company