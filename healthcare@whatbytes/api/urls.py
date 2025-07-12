from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),

    path('patients/', PatientListCreate.as_view()),
    path('patients/<int:pk>/', PatientDetail.as_view()),

    path('doctors/', DoctorListCreate.as_view()),
    path('doctors/<int:pk>/', DoctorDetail.as_view()),

    path('mappings/', MappingListCreate.as_view()),
    path('mappings/<int:pk>/', MappingDetail.as_view()),
    path('mappings/patient/<int:patient_id>/', PatientMappings.as_view()),
]
