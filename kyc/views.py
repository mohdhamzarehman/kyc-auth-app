from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.utils import timezone
from .models import KYCDocument
from .serializers import KYCDocumentSerializer

# Create your views here.

class KYCDocumentUploadView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = KYCDocumentSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class KYCDocumentListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = KYCDocumentSerializer

    def get_queryset(self):
        return KYCDocument.objects.filter(user=self.request.user)

class KYCDocumentDetailView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = KYCDocumentSerializer
    
    def get_queryset(self):
        return KYCDocument.objects.filter(user=self.request.user)

class KYCVerificationStatusView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        user = request.user
        documents = KYCDocument.objects.filter(user=user)
        
        status_data = {
            'is_kyc_verified': user.is_kyc_verified,
            'verification_date': user.kyc_verification_date,
            'documents': [{
                'type': doc.document_type,
                'status': doc.verification_status,
                'uploaded_at': doc.uploaded_at,
                'verified_at': doc.verified_at,
                'rejection_reason': doc.rejection_reason
            } for doc in documents]
        }
        
        return Response(status_data)
