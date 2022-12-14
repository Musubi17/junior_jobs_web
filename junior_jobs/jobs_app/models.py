from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=255)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()

    def __str__(self):
        return self.name


class Specialty(models.Model):
    code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    picture = models.URLField(default='https://place-hold.it/100x60')

    def __str__(self):
        return self.title
