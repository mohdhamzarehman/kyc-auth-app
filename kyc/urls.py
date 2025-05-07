from django.urls import path
from .views import (
    KYCDocumentUploadView,
    KYCDocumentListView,
    KYCDocumentDetailView,
    KYCVerificationStatusView
)

urlpatterns = [
    path('upload/', KYCDocumentUploadView.as_view(), name='kyc-upload'),
    path('documents/', KYCDocumentListView.as_view(), name='kyc-documents'),
    path('documents/<int:pk>/', KYCDocumentDetailView.as_view(), name='kyc-document-detail'),
    path('status/', KYCVerificationStatusView.as_view(), name='kyc-status'),
] 