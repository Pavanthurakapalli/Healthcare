
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied, ValidationError
from django.shortcuts import get_object_or_404
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import *
 
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
 
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
 
 
class PatientListCreate(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
 
 
class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)
 
    def get_object(self):
        try:
            obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
            return obj
        except:
            raise NotFound("Patient not found or access denied.")
 
    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
 
 
class DoctorListCreate(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
 
 
class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    def get_object(self):
        try:
            return get_object_or_404(Doctor, pk=self.kwargs['pk'])
        except:
            raise NotFound("Doctor not found.")
 
 
class MappingListCreate(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
 
 
class MappingDetail(generics.RetrieveDestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    def get_object(self):
        try:
            return get_object_or_404(PatientDoctorMapping, pk=self.kwargs['pk'])
        except:
            raise NotFound("Mapping not found.")
 
 
class PatientMappings(generics.ListAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')
        if not Patient.objects.filter(pk=patient_id).exists():
            raise NotFound("Patient not found.")
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)
 
 