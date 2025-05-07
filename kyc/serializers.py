from rest_framework import serializers
from .models import KYCDocument

class KYCDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYCDocument
        fields = ('id', 'document_type', 'document_file', 'verification_status',
                 'uploaded_at', 'verified_at', 'rejection_reason')
        read_only_fields = ('verification_status', 'uploaded_at', 'verified_at',
                          'rejection_reason')

    def validate_document_file(self, value):
        # Validate file size (max 5MB)
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("File size cannot exceed 5MB")
        allowed_types = ['application/pdf', 'image/jpeg', 'image/png']
        if value.content_type not in allowed_types:
            raise serializers.ValidationError(
                "File type not supported. Please upload PDF, JPEG, or PNG files."
            )
        return value 