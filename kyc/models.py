from django.db import models
from django.conf import settings

class KYCDocument(models.Model):
    DOCUMENT_TYPES = (
        ('passport', 'Passport'),
        ('id_card', 'ID Card'),
        ('drivers_license', 'Driver\'s License'),
        ('utility_bill', 'Utility Bill'),
    )
    
    VERIFICATION_STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='kyc_documents')
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    document_file = models.FileField(upload_to='kyc_documents/%Y/%m/%d/')
    verification_status = models.CharField(max_length=10, choices=VERIFICATION_STATUS, default='pending')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    rejection_reason = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.document_type} - {self.verification_status}"
