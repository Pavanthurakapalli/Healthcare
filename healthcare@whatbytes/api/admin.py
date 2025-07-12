from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Patient, Doctor, PatientDoctorMapping

# Custom User Admin
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['email', 'username', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser']
    search_fields = ['email', 'username']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

# ✅ Inline to show assigned doctors inside Patient admin
class PatientDoctorMappingInline(admin.TabularInline):
    model = PatientDoctorMapping
    extra = 0
    verbose_name = "Assigned Doctor"
    verbose_name_plural = "Assigned Doctors"

# ✅ Patient admin with inline for doctor mapping
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'user')
    #inlines = [PatientDoctorMappingInline]

# Register models
admin.site.register(User, UserAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor)
admin.site.register(PatientDoctorMapping)
