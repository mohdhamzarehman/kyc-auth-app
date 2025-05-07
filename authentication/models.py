from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_kyc_verified = models.BooleanField(default=False)
    kyc_verification_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'auth_user'
        
    def __str__(self):
        return self.email or self.username
