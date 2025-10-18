from django.db import models
from django.contrib.auth.models import User

class Depo(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Train(models.Model):
    number = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    depo = models.ForeignKey(Depo, on_delete=models.CASCADE)
    def __str__(self):
        return f"Поезд {self.number} ({self.depo})"

class Wagon(models.Model):
    number = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.number

class TrainWagon(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    wagon = models.ForeignKey(Wagon, on_delete=models.CASCADE)

class Remark(models.Model):
    STATUS_CHOICES = [('open','Не устранено'), ('closed','Устранено')]
    wagon = models.ForeignKey(Wagon, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    date_found = models.DateField(auto_now_add=True)
    date_fixed = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.wagon} - {self.description[:30]} ({self.status})"
