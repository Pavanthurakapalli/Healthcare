from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError
 
class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
 
    def __str__(self):
        return self.email
 
 
class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    condition = models.TextField()
 
    def __str__(self):
        return f"{self.name} (Age: {self.age})"
 
    def clean(self):
        if self.age < 0:
            raise ValidationError("Age cannot be negative.")
        if self.gender not in dict(self.GENDER_CHOICES):
            raise ValidationError("Invalid gender selection.")
 
 
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
 
    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"
 
 
class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
 
    class Meta:
        unique_together = ('patient', 'doctor')  # prevents duplicate mappings
 
    def __str__(self):
        return f"{self.patient.name} ↔ {self.doctor.name}"