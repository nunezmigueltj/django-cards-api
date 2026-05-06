from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=150)
    grade = models.IntegerField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return f"{self.name} ({self.grade}) - {self.company.name}"