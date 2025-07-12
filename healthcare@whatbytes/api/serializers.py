from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping, User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
 
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
 
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
 
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value
 
    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
            return user
        except DjangoValidationError as e:
            raise serializers.ValidationError({"password": e.messages})
 
 
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['user']
 
    def validate_age(self, value):
        if value < 0 or value > 120:
            raise serializers.ValidationError("Age must be between 0 and 120.")
        return value
 
    def validate_gender(self, value):
        allowed = ['Male', 'Female', 'Other']
        if value not in allowed:
            raise serializers.ValidationError(f"Gender must be one of {allowed}.")
        return value
 
 
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
 
    def validate_email(self, value):
        if Doctor.objects.filter(email=value).exists():
            raise serializers.ValidationError("A doctor with this email already exists.")
        return value
 
 
class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
 
    def validate(self, data):
        patient = data.get('patient')
        doctor = data.get('doctor')
 
        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError("This mapping already exists.")
 
        return data